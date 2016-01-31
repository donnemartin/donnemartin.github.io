Title: Python Hadoop MapReduce: Analyzing AWS S3 Bucket Logs with mrjob
Date: 2015-05-17
Summary: mrjob lets you write MapReduce jobs in Python 2.5+ and run them on several platforms.
tags: Data, Cloud
CoverImage: https://raw.githubusercontent.com/donnemartin/donnemartin.github.io/master/images/posts/mrjob_cover.png
Thumbnail: http://i1.wp.com/donnemartin.net/wp-content/uploads/2015/05/mrjob_cover.png?zoom=2&resize=320%2C202

## Introduction

mrjob lets you write MapReduce jobs in Python 2.5+ and run them on several platforms. You can:

Write multi-step MapReduce jobs in pure Python
Test on your local machine
Run on a Hadoop cluster
Run in the cloud using Amazon Elastic MapReduce (EMR)

## Setup

From PyPI:

```
pip install mrjob
```

From source:

```
python setup.py install
```

See "Sample .mrjob.conf" section below for additional config details.


## Processing S3 Logs

Sample mrjob code that processes log files on Amazon S3 based on the S3 logging format:

```
mr_s3_log_parser.py

import time
from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol, ReprProtocol
import re


class MrS3LogParser(MRJob):
    """Parses the logs from S3 based on the S3 logging format:
    http://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html

    Aggregates a user's daily requests by user agent and operation

    Outputs date_time, requester, user_agent, operation, count
    """

    LOGPATS  = r'(\S+) (\S+) \[(.*?)\] (\S+) (\S+) ' \
               r'(\S+) (\S+) (\S+) ("([^"]+)"|-) ' \
               r'(\S+) (\S+) (\S+) (\S+) (\S+) (\S+) ' \
               r'("([^"]+)"|-) ("([^"]+)"|-)'
    NUM_ENTRIES_PER_LINE = 17
    logpat = re.compile(LOGPATS)

    (S3_LOG_BUCKET_OWNER,
     S3_LOG_BUCKET,
     S3_LOG_DATE_TIME,
     S3_LOG_IP,
     S3_LOG_REQUESTER_ID,
     S3_LOG_REQUEST_ID,
     S3_LOG_OPERATION,
     S3_LOG_KEY,
     S3_LOG_HTTP_METHOD,
     S3_LOG_HTTP_STATUS,
     S3_LOG_S3_ERROR,
     S3_LOG_BYTES_SENT,
     S3_LOG_OBJECT_SIZE,
     S3_LOG_TOTAL_TIME,
     S3_LOG_TURN_AROUND_TIME,
     S3_LOG_REFERER,
     S3_LOG_USER_AGENT) = range(NUM_ENTRIES_PER_LINE)

    DELIMITER = '\t'

    # We use RawValueProtocol for input to be format agnostic
    # and avoid any type of parsing errors
    INPUT_PROTOCOL = RawValueProtocol

    # We use RawValueProtocol for output so we can output raw lines
    # instead of (k, v) pairs
    OUTPUT_PROTOCOL = RawValueProtocol

    # Encode the intermediate records using repr() instead of JSON, so the
    # record doesn't get Unicode-encoded
    INTERNAL_PROTOCOL = ReprProtocol

    def clean_date_time_zone(self, raw_date_time_zone):
        """Converts entry 22/Jul/2013:21:04:17 +0000 to the format
        'YYYY-MM-DD HH:MM:SS' which is more suitable for loading into
        a database such as Redshift or RDS

        Note: requires the chars "[ ]" to be stripped prior to input
        Returns the converted datetime annd timezone
        or None for both values if failed

        TODO: Needs to combine timezone with date as one field
        """
        date_time = None
        time_zone_parsed = None

        # TODO: Probably cleaner to parse this with a regex
        date_parsed = raw_date_time_zone[:raw_date_time_zone.find(":")]
        time_parsed = raw_date_time_zone[raw_date_time_zone.find(":") + 1:
                                         raw_date_time_zone.find("+") - 1]
        time_zone_parsed = raw_date_time_zone[raw_date_time_zone.find("+"):]

        try:
            date_struct = time.strptime(date_parsed, "%d/%b/%Y")
            converted_date = time.strftime("%Y-%m-%d", date_struct)
            date_time = converted_date + " " + time_parsed

        # Throws a ValueError exception if the operation fails that is
        # caught by the calling function and is handled appropriately
        except ValueError as error:
            raise ValueError(error)
        else:
            return converted_date, date_time, time_zone_parsed

    def mapper(self, _, line):
        line = line.strip()
        match = self.logpat.search(line)

        date_time = None
        requester = None
        user_agent = None
        operation = None

        try:
            for n in range(self.NUM_ENTRIES_PER_LINE):
                group = match.group(1 + n)

                if n == self.S3_LOG_DATE_TIME:
                    date, date_time, time_zone_parsed = \
                        self.clean_date_time_zone(group)
                    # Leave the following line of code if
                    # you want to aggregate by date
                    date_time = date + " 00:00:00"
                elif n == self.S3_LOG_REQUESTER_ID:
                    requester = group
                elif n == self.S3_LOG_USER_AGENT:
                    user_agent = group
                elif n == self.S3_LOG_OPERATION:
                    operation = group
                else:
                    pass

        except Exception:
            yield (("Error while parsing line: %s", line), 1)
        else:
            yield ((date_time, requester, user_agent, operation), 1)

    def reducer(self, key, values):
        output = list(key)
        output = self.DELIMITER.join(output) + \
                 self.DELIMITER + \
                 str(sum(values))

        yield None, output

    def steps(self):
        return [
            self.mr(mapper=self.mapper,
                    reducer=self.reducer)
        ]


if __name__ == '__main__':
    MrS3LogParser.run()
```

## Running Amazon Elastic MapReduce (EMR) Jobs

Run an Amazon EMR job on the given input (must be a flat file hierarchy), placing the results in the output (output directory must not exist):

```
python mr-mr_s3_log_parser.py -r emr s3://bucket-source/ --output-dir=s3://bucket-dest/
```

Run a MapReduce job locally on the specified input file, sending the results to the specified output file:

```
python mr_s3_log_parser.py input_data.txt > output_data.txt
```

## Unit Testing S3 Logs

Accompanying unit test:

```
test_mr_s3_log_parser.py

from StringIO import StringIO
import unittest2 as unittest
from mr_s3_log_parser import MrS3LogParser


class MrTestsUtil:

    def run_mr_sandbox(self, mr_job, stdin):
        # inline runs the job in the same process so small jobs tend to
        # run faster and stack traces are simpler
        # --no-conf prevents options from local mrjob.conf from polluting
        # the testing environment
        # "-" reads from standard in
        mr_job.sandbox(stdin=stdin)

        # make_runner ensures job cleanup is performed regardless of
        # success or failure
        with mr_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                key, value = mr_job.parse_output_line(line)
                yield value


class TestMrS3LogParser(unittest.TestCase):

    mr_job = None
    mr_tests_util = None

    RAW_LOG_LINE_INVALID = \
        '00000fe9688b6e57f75bd2b7f7c1610689e8f01000000' \
        '00000388225bcc00000 ' \
        's3-storage [22/Jul/2013:21:03:27 +0000] ' \
        '00.111.222.33 ' \

    RAW_LOG_LINE_VALID = \
        '00000fe9688b6e57f75bd2b7f7c1610689e8f01000000' \
        '00000388225bcc00000 ' \
        's3-storage [22/Jul/2013:21:03:27 +0000] ' \
        '00.111.222.33 ' \
        'arn:aws:sts::000005646931:federated-user/user 00000AB825500000 ' \
        'REST.HEAD.OBJECT user/file.pdf ' \
        '"HEAD /user/file.pdf?versionId=00000XMHZJp6DjM9x500000' \
        '00000SDZk ' \
        'HTTP/1.1" 200 - - 4000272 18 - "-" ' \
        '"Boto/2.5.1 (darwin) USER-AGENT/1.0.14.0" ' \
        '00000XMHZJp6DjM9x5JVEAMo8MG00000'

    DATE_TIME_ZONE_INVALID = "AB/Jul/2013:21:04:17 +0000"
    DATE_TIME_ZONE_VALID = "22/Jul/2013:21:04:17 +0000"
    DATE_VALID = "2013-07-22"
    DATE_TIME_VALID = "2013-07-22 21:04:17"
    TIME_ZONE_VALID = "+0000"

    def __init__(self, *args, **kwargs):
        super(TestMrS3LogParser, self).__init__(*args, **kwargs)
        self.mr_job = MrS3LogParser(['-r', 'inline', '--no-conf', '-'])
        self.mr_tests_util = MrTestsUtil()

    def test_invalid_log_lines(self):
        stdin = StringIO(self.RAW_LOG_LINE_INVALID)

        for result in self.mr_tests_util.run_mr_sandbox(self.mr_job, stdin):
            self.assertEqual(result.find("Error"), 0)

    def test_valid_log_lines(self):
        stdin = StringIO(self.RAW_LOG_LINE_VALID)

        for result in self.mr_tests_util.run_mr_sandbox(self.mr_job, stdin):
            self.assertEqual(result.find("Error"), -1)

    def test_clean_date_time_zone(self):
        date, date_time, time_zone_parsed = \
            self.mr_job.clean_date_time_zone(self.DATE_TIME_ZONE_VALID)
        self.assertEqual(date, self.DATE_VALID)
        self.assertEqual(date_time, self.DATE_TIME_VALID)
        self.assertEqual(time_zone_parsed, self.TIME_ZONE_VALID)

        # Use a lambda to delay the calling of clean_date_time_zone so that
        # assertRaises has enough time to handle it properly
        self.assertRaises(ValueError,
            lambda: self.mr_job.clean_date_time_zone(
                self.DATE_TIME_ZONE_INVALID))

if __name__ == '__main__':
    unittest.main()
```

## Running S3 Logs Unit Test

Run the mrjob test:

```
python test_mr_s3_log_parser.py -v
```

## Sample .mrjob.conf

```
runners:
  emr:
    aws_access_key_id: __ACCESS_KEY__
    aws_secret_access_key: __SECRET_ACCESS_KEY__
    aws_region: us-east-1
    ec2_key_pair: EMR
    ec2_key_pair_file: ~/.ssh/EMR.pem
    ssh_tunnel_to_job_tracker: true
    ec2_master_instance_type: m1.small
    ec2_instance_type: m1.small
    num_ec2_instances: 5
    s3_scratch_uri: s3://bucket/tmp/
    s3_log_uri: s3://bucket/tmp/logs/
    enable_emr_debugging: True
    bootstrap:
    - sudo apt-get install -y python-pip
    - sudo pip install --upgrade simplejson
```
