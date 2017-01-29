Title: Speeding Up Hadoop MapReduce Jobs with S3DistCp
Date: 2014-12-20
Summary: Input file size has a significant impact on the job length, due to the mapper setup time.
Tags: Cloud, Data
CoverImage: https://raw.githubusercontent.com/donnemartin/donnemartin.github.io/master/images/posts/hadoop_emr_cover.png
Thumbnail: http://i0.wp.com/donnemartin.net/wp-content/uploads/2014/12/hadoop_emr_cover.png?zoom=2&resize=320%2C202

When optimizing Hadoop MapReduce jobs on AWS Elastic Map Reduce, you often tweak the EC2 instance type and number of instances to obtain the optimal number of mappers.  More data = more splits = more mappers.  [EC2 instances vary](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/TaskConfiguration.html) in the number of mappers they can support in parallel--for example an m1.XL can process 6-8 mappers in parallel, whereas an m1.small can only run up to 2 mappers in parallel.

Input file size can also have a significant impact on the job length, due to slow disk seek speeds and mapper setup times.

## Mapper Setup Time

The following stats demonstrate why small files are so problematic with Hadoop:

* Each mapper is a single Java Virtual Machine (JVM) which needs CPU and memory resources
* Mappers take 2 seconds to spawn up and be ready for processing
* 10,000 mappers * 2 seconds = 5 hours of mapper CPU setup time
* 100,000 mappers * 2 seconds = 55 hours of mapper CPU setup time

As an aside, Spark does not start a new JVM for each mapper task, it uses a JVM for each executor.  Executors can run multiple tasks and stay up for the life of an application.

## Optimal Input File Size

Due to the relatively lengthy setup time for mappers, you generally want a mapper and its associated JVM to stay for as long as possible.  Ideally, each mapper should have a minimum life span of at least 60 seconds.  Since a single mapper can get 10 MB to 15 MB per second speed to Amazon S3, the ideal file size is 60 sec * 15 MB which is roughly 1 GB.

Thus, **Amazon recommends input files to be between 1GB to 2GB**.  Unfortunately, many log files are typically nowhere near this range.

How do you merge your files to fall within this 1 GB to 2 GB sweet spot?

## DistCp and S3DistCp

[Apache DistCp](http://hadoop.apache.org/docs/r1.2.1/distcp.html) is an open-source tool that uses MapReduce under the hood to copy large amounts of data.

[S3DistCp](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/UsingEMR_s3distcp.html) is an extension of DistCp that is optimized to work with Amazon S3.  S3DistCp is useful for combining smaller files and aggregate them together, taking in a pattern and target file to combine smaller input files to larger ones.  S3DistCp can also be used to transfer large volumes of data from S3 to your Hadoop cluster.

S3DistCp can be used with the [EMR CLI](http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-cli-install.html)

## S3DistCp Code

The EMR command line below executes the following:

* Create a master node and slave nodes of type m1.small
* Runs S3DistCp on the source bucket location and concatenates files that match the date regular expression, resulting in files that are roughly 1024 MB or 1 GB
* Places the results in the destination bucket

```
./elastic-mapreduce --create --instance-group master --instance-count 1 \
--instance-type m1.small --instance-group core --instance-count 4 \
--instance-type m1.small --jar /home/hadoop/lib/emr-s3distcp-1.0.jar \
--args "--src,s3://my-bucket-source/,--groupBy,.*([0-9]{4}-01).*,\
--dest,s3://my-bucket-dest/,--targetSize,1024"
```

## A Note on Compression

For further optimization, compression can be helpful to save on AWS storage and bandwidth costs, to speed up the S3 to/from EMR transfer, and to reduce disk I/O.  Note that compressed files are not easy to split for Hadoop.  For example, Hadoop uses a single mapper per GZIP file, as it does not know about file boundaries.

What type of compression should you use?

* Time sensitive job: Snappy or LZO
* Large amounts of data: GZIP
* General purpose: GZIP, as it's supported by most platforms

You can specify the compression codec (gzip, lzo, snappy, or none) to use for copied files with S3DistCp with --outputCodec.  If no value is specified, files are copied with no compression change.  The code below sets the compression to lzo:

```
--outputCodec,lzo
```
