Title: S3cmd: Frequently Used Commands
Date: 2014-12-04
Summary: I’ve found S3cmd to be a great tool for interacting with S3 on AWS.  S3cmd is written in Python, is open source, and is free even for commercial use.
Tags: Cloud, Data
CoverImage: https://raw.githubusercontent.com/donnemartin/donnemartin.github.io/master/images/posts/terminal2_cover.png
Thumbnail: http://i2.wp.com/donnemartin.net/wp-content/uploads/2014/12/terminal2_cover.png?zoom=2&resize=320%2C202

Before I discovered [S3cmd](http://s3tools.org/s3cmd), I had been using the [S3 console](http://aws.amazon.com/console/) to do basic operations and [boto](https://boto.readthedocs.org/en/latest/) to do more of the heavy lifting.  However, sometimes I just want to hack away at a command line to do my work.

## S3cmd

I've found S3cmd to be a great command line tool for interacting with S3 on AWS.  S3cmd is written in Python, is open source, and is free even for commercial use.  It offers more advanced features than those found in the [AWS CLI](http://aws.amazon.com/cli/).

## Configuring S3cmd

Running the following command will prompt you to enter your AWS access and AWS secret keys. To follow security best practices, make sure you are using an IAM account as opposed to using the root account.

```
s3cmd --configure
```

I also suggest enabling GPG encryption which will encrypt your data at rest, and enabling HTTPS to encrypt your data in transit.  Note this might impact performance.

## Frequently Used Commands

```
# List all buckets
s3cmd ls

# List the contents of the bucket
s3cmd ls s3://my-bucket-name

# Upload a file into the bucket (private)
s3cmd put myfile.txt s3://my-bucket-name/myfile.txt

# Upload a file into the bucket (public)
s3cmd put --acl-public --guess-mime-type myfile.txt s3://my-bucket-name/myfile.txt

# Recursively upload a directory to s3
s3cmd put --recursive my-local-folder-path/ s3://my-bucket-name/mydir/

# Download a file
s3cmd get s3://my-bucket-name/myfile.txt myfile.txt

# Recursively download files that start with myfile
s3cmd --recursive get s3://my-bucket-name/myfile

# Delete a file
s3cmd del s3://my-bucket-name/myfile.txt

# Delete a bucket
s3cmd del --recursive s3://my-bucket-name/

# Create a bucket
s3cmd mb s3://my-bucket-name

# List bucket disk usage (human readable)
s3cmd du -H s3://my-bucket-name/

# Sync local (source) to s3 bucket (destination)
s3cmd sync my-local-folder-path/ s3://my-bucket-name/

# Sync s3 bucket (source) to local (destination)
s3cmd sync s3://my-bucket-name/ my-local-folder-path/

# Do a dry-run (do not perform actual sync, but get information about what would happen)
s3cmd --dry-run sync s3://my-bucket-name/ my-local-folder-path/

# Apply a standard shell wildcard include to sync s3 bucket (source) to local (destination)
s3cmd --include '2014-05-01*' sync s3://my-bucket-name/ my-local-folder-path/
```
