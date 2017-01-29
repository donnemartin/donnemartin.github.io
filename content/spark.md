Title: Apache Spark Tutorial
Date: 2016-06-19
Summary: Hands-on introduction with PySpark.
Tags: Python
CoverImage: http://i.imgur.com/Ud8lvyp.png
Thumbnail: http://i.imgur.com/i9Ag5ec.png

# Spark

* IPython Notebook Setup
* Python Shell
* DataFrames
* RDDs
* Pair RDDs
* Running Spark on a Cluster
* Viewing the Spark Application UI
* Working with Partitions
* Caching RDDs
* Checkpointing RDDs
* Writing and Running a Spark Application
* Configuring Spark Applications
* Streaming
* Streaming with States
* Broadcast Variables
* Accumulators

## IPython Notebook Setup

The [dev-setup](https://github.com/donnemartin/dev-setup) repo contains scripts to install Spark and to automate the its integration with IPython Notebook through the [pydata.sh script](https://github.com/donnemartin/dev-setup/blob/master/aws.sh).

You can also follow the instructions provided [here](http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/) to configure IPython Notebook Support for PySpark with Python 2.

To run Python 3 with Spark 1.4+, check out the following posts on [Stack Overflow](http://stackoverflow.com/questions/30279783/apache-spark-how-to-use-pyspark-with-python-3) or [Reddit](http://www.reddit.com/r/datascience/comments/3ar1bd/continually_updated_data_science_python_notebooks/).

## Python Shell

Start the pyspark shell (REPL):


```python
pyspark
```

View the spark context, the main entry point to the Spark API:


```python
sc
```

## DataFrames

From the following [reference](https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html):

A DataFrame is a distributed collection of data organized into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations under the hood.

Create a DataFrame from JSON files on S3:


```python
users = context.load("s3n://path/to/users.json", "json")
```

Create a new DataFrame that contains “young users” only:


```python
young = users.filter(users.age<21)
```

Alternatively, using Pandas-like syntax:


```python
young = users[users.age<21]
```

Increment everybody’s age by 1:


```python
young.select(young.name, young.age+1)
```

Count the number of young users by gender:


```python
young.groupBy("gender").count()
```

Join young users with another DataFrame called logs:


```python
young.join(logs, logs.userId == users.userId, "left_outer")
```

Count the number of users in the young DataFrame:


```python
young.registerTempTable("young")
context.sql("SELECT count(*) FROM young")
```

Convert Spark DataFrame to Pandas:


```python
pandas_df = young.toPandas()
```

Create a Spark DataFrame from Pandas:


```python
spark_df = context.createDataFrame(pandas_df)
```

Given the Spark Context, create a SQLContext:


```python
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
```

Create a DataFrame based on the content of a file:


```python
df = sqlContext.jsonFile("file:/path/file.json")
```

Display the content of the DataFrame:


```python
df.show()
```

Print the schema:


```python
df.printSchema()
```

Select a column:


```python
df.select("column_name")
```

Create a DataFrame with rows matching a given filter:


```python
df.filter(df.column_name>10)
```

Aggregate the results and count:


```python
df.groupBy("column_name").count()
```

Convert a RDD to a DataFrame (by inferring the schema):


```python
df = sqlContext.inferSchema(my_data)
```

Register the DataFrame as a table:


```python
df.registerTempTable("dataframe_name")
```

Run a SQL Query on a DataFrame registered as a table:


```python
rdd_from_df = sqlContext.sql("SELECT * FROM dataframe_name")
```

## RDDs

Note: RDDs are included for completeness.  In Spark 1.3, DataFrames were introduced which are recommended over RDDs.  Check out the [DataFrames announcement](https://databricks.com/blog/2015/02/17/introducing-dataframes-in-spark-for-large-scale-data-science.html) for more info.

Resilient Distributed Datasets (RDDs) are the fundamental unit of data in Spark.  RDDs can be created from a file, from data in memory, or from another RDD.  RDDs are immutable.

There are two types of RDD operations:
* Actions: Returns values, data is not processed in an RDD until an action is preformed
* Transformations: Defines a new RDD based on the current


Create an RDD from the contents of a directory:


```python
my_data = sc.textFile("file:/path/*")
```

Count the number of lines in the data:


```python
my_data.count()
```

Return all the elements of the dataset as an array--this is usually more useful after a filter or other operation that returns a sufficiently small subset of the data:


```python
my_data.collect()
```

Return the first 10 lines in the data:


```python
my_data.take(10)
```

Create an RDD with lines matching the given filter:


```python
my_data.filter(lambda line: ".txt" in line)
```

Chain a series of commands:


```python
sc.textFile("file:/path/file.txt") \
    .filter(lambda line: ".txt" in line) \
    .count()
```

Create a new RDD mapping each line to an array of words, taking only the first word of each array:


```python
first_words = my_data.map(lambda line: line.split()[0])
```

Output each word in first_words:


```python
for word in first_words.take(10):
    print word
```

Save the first words to a text file:


```python
first_words.saveAsTextFile("file:/path/file")
```

## Pair RDDs

Pair RDDs contain elements that are key-value pairs.  Keys and values can be any type.

Given a log file with the following space deilmited format: [date_time, user_id, ip_address, action], map each request to (user_id, 1):


```python
DATE_TIME = 0
USER_ID = 1
IP_ADDRESS = 2
ACTION = 3

log_data = sc.textFile("file:/path/*")

user_actions = log_data \
    .map(lambda line: line.split()) \
    .map(lambda words: (words[USER_ID], 1))  \
    .reduceByKey(lambda count1, count2: count1 + count2)
```

Show the top 5 users by count, sorted in descending order:


```python
user_actions.map(lambda pair: (pair[0], pair[1])).sortyByKey(False).take(5)
```

Group IP addresses by user id:


```python
user_ips = log_data \
    .map(lambda line: line.split()) \
    .map(lambda words: (words[IP_ADDRESS],words[USER_ID])) \
    .groupByKey()
```

Given a user table with the following csv format: [user_id, user_info0, user_info1, ...], map each line to (user_id, [user_info...]):


```python
user_data = sc.textFile("file:/path/*")

user_profile = user_data \
    .map(lambda line: line.split(',')) \
    .map(lambda words: (words[0], words[1:]))
```

Inner join the user_actions and user_profile RDDs:


```python
user_actions_with_profile = user_actions.join(user_profile)
```

Show the joined table:


```python
for (user_id, (user_info, count)) in user_actions_with_profiles.take(10):
    print user_id, count, user_info
```

## Running Spark on a Cluster

Start the standalone cluster's Master and Worker daemons:


```python
sudo service spark-master start
sudo service spark-worker start
```

Stop the standalone cluster's Master and Worker daemons:


```python
sudo service spark-master stop
sudo service spark-worker stop
```

Restart the standalone cluster's Master and Worker daemons:


```python
sudo service spark-master stop
sudo service spark-worker stop
```

View the Spark standalone cluster UI:


```python
http://localhost:18080//
```

Start the Spark shell and connect to the cluster:


```python
MASTER=spark://localhost:7077 pyspark
```

Confirm you are connected to the correct master:


```python
sc.master
```

## Viewing the Spark Application UI

From the following [reference](http://spark.apache.org/docs/1.2.0/monitoring.html):

Every SparkContext launches a web UI, by default on port 4040, that displays useful information about the application. This includes:

A list of scheduler stages and tasks
A summary of RDD sizes and memory usage
Environmental information.
Information about the running executors

You can access this interface by simply opening http://<driver-node>:4040 in a web browser. If multiple SparkContexts are running on the same host, they will bind to successive ports beginning with 4040 (4041, 4042, etc).

Note that this information is only available for the duration of the application by default. To view the web UI after the fact, set spark.eventLog.enabled to true before starting the application. This configures Spark to log Spark events that encode the information displayed in the UI to persisted storage.


```python
http://localhost:4040/
```

## Working with Partitions

From the following [reference](http://blog.cloudera.com/blog/2014/09/how-to-translate-from-mapreduce-to-apache-spark/):

The Spark map() and flatMap() methods only operate on one input at a time, and provide no means to execute code before or after transforming a batch of values. It looks possible to simply put the setup and cleanup code before and after a call to map() in Spark:


```python
val dbConnection = ...
lines.map(... dbConnection.createStatement(...) ...)
dbConnection.close() // Wrong!
```

However, this fails for several reasons:

* It puts the object dbConnection into the map function’s closure, which requires that it be serializable (for example, by implementing java.io.Serializable). An object like a database connection is generally not serializable.
* map() is a transformation, rather than an operation, and is lazily evaluated. The connection can’t be closed immediately here.
* Even so, it would only close the connection on the driver, not necessarily freeing resources allocated by serialized copies.

In fact, neither map() nor flatMap() is the closest counterpart to a Mapper in Spark — it’s the important mapPartitions() method. This method does not map just one value to one other value, but rather maps an Iterator of values to an Iterator of other values. It’s like a “bulk map” method. This means that the mapPartitions() function can allocate resources locally at its start, and release them when done mapping many values.


```python
def count_txt(partIter):
    for line in partIter:
        if ".txt" in line: txt_count += 1
    yield (txt_count)

my_data = sc.textFile("file:/path/*") \
    .mapPartitions(count_txt) \
    .collect()

# Show the partitioning
print "Data partitions: ", my_data.toDebugString()
```

## Caching RDDs

Caching an RDD saves the data in memory.  Caching is a suggestion to Spark as it is memory dependent.

By default, every RDD operation executes the entire lineage.  Caching can boost performance for datasets that are likely to be used by saving this expensive recomputation and is ideal for iterative algorithms or machine learning.

* cache() stores data in memory
* persist() stores data in MEMORY_ONLY, MEMORY_AND_DISK (spill to disk), and  DISK_ONLY

Disk memory is stored on the node, not on HDFS.

Replication is possible by using MEMORY_ONLY_2, MEMORY_AND_DISK_2, etc.  If a cached partition becomes unavailable, Spark recomputes the partition through the lineage.

Serialization is possible with MEMORY_ONLY_SER and MEMORY_AND_DISK_SER.  This is more space efficient but less time efficient, as it uses Java serialization by default.


```python
# Cache RDD to memory
my_data.cache()

# Persist RDD to both memory and disk (if memory is not enough), with replication of 2
my_data.persist(MEMORY_AND_DISK_2)

# Unpersist RDD, removing it from memory and disk
my_data.unpersist()

# Change the persistence level after unpersist
my_data.persist(MEMORY_AND_DISK)
```

## Checkpointing RDDs

Caching maintains RDD lineage, providing resilience.  If the lineage is very long, it is possible to get a stack overflow.

Checkpointing saves the data to HDFS, which provide fault tolerant storage across nodes.  HDFS is not as fast as local storage for both reading and writing.  Checkpointing is good for long lineages and for very large data sets that might not fit on local storage.  Checkpointing removes lineage.

Create a checkpoint and perform an action by calling count() to materialize the checkpoint and save it to the checkpoint file:


```python
# Enable checkpointing by setting the checkpoint directory,
# which will contain all checkpoints for the given data:
sc.setCheckpointDir("checkpoints")

my_data = sc.parallelize([1,2,3,4,5])

# Long loop that may cause a stack overflow
for i in range(1000):
    my_data = mydata.map(lambda myInt: myInt + 1)

    if i % 10 == 0:
        my_data.checkpoint()
        my_data.count()

my_data.collect()

# Display the lineage
for rddstring in my_data.toDebugString().split('\n'):
    print rddstring.strip()
```

## Writing and Running a Spark Application

Create a Spark application to count the number of text files:


```python
import sys
from pyspark import SparkContext

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: App Name <file>"
        exit(-1)

    count_text_files()

def count_text_files():
    sc = SparkContext()
    logfile = sys.argv[1]
    text_files_count = sc.textFile(logfile)
        .filter(lambda line: '.txt' in line)
    text_files_count.cache()
    print("Number of text files: ", text_files_count.count())
```

Submit the script to Spark for processing:


```python
spark-submit --properties-file dir/myspark.conf script.py data/*
```

## Configuring Spark Applications

Run a Spark app and set the configuration options in the command line:


```python
spark-submit --master spark//localhost:7077 --name 'App Name' script.py data/*
```

Configure spark.conf:


```python
spark.app.name  App Name
spark.ui.port   4141
spark.master    spark://localhost:7077
```

Run a Spark app and set the configuration options through spark.conf:


```python
spark-submit --properties-file spark.conf script.py data/*
```

Set the config options programmatically:


```python
sconf = SparkConf() \
    .setAppName("Word Count") \
    .set("spark.ui.port","4141")
sc = SparkContext(conf=sconf)
```

Set logging levels located in the following file, or place a copy in your pwd:


```python
$SPARK_HOME/conf/log4j.properties.template
```

## Streaming

Start the Spark Shell locally with at least two threads (need a minimum of two threads for streaming, one for receiving, one for processing):


```python
spark-shell --master local[2]
```

Create a StreamingContext (similar to SparkContext in core Spark) with a batch duration of 1 second:


```python
val ssc = new StreamingContext(new SparkConf(), Seconds(1))
val my_stream = ssc.socketTextStream(hostname, port)
```

Get a DStream from a streaming data source (text from a socket):


```python
val logs = ssc.socketTextStream(hostname, port)
```

DStreams support regular transformations such as map, flatMap, and filter, and pair transformations such as reduceByKey, groupByKey, and joinByKey.

Apply a DStream operation to each batch of RDDs (count up requests by user id, reduce by key to get the count):


```python
val requests = my_stream
    .map(line => (line.split(" ")(2), 1))
    .reduceByKey((x, y) => x + y)
```

The transform(function) method creates a new DStream by executing the input function on the RDDs.


```python
val sorted_requests = requests
    .map(pair => pair.swap)
    .transform(rdd => rdd.sortByKey(false))
```

foreachRDD(function) performs a function on each RDD in the DStream (map is like a shortcut not requiring you to get the RDD first before doing an operation):


```python
sorted_requests.foreachRDD((rdd, time) => {
    println("Top users @ " + time)
    rdd.take(5).foreach(
    pair => printf("User: %s (%s)\n", pair._2, pair._1))
}
```

Save the DStream result part files with the given folder prefix, the actual folder will be /dir/requests-timestamp0/:


```python
requests.saveAsTextFiles("/dir/requests")
```

Start the execution of all DStreams:


```python
ssc.start()
```

Wait for all background threads to complete before ending the main thread:


```python
ssc.awaitTermination()
```

## Streaming with States

Enable checkpointing to prevent infinite lineages:


```python
ssc.checkpoint("dir")
```

Compute a DStream based on the previous states plus the current state:


```python
def updateCount = (newCounts: Seq[Int], state: Option[Int]) => {
    val newCount = newCounts.foldLeft(0)(_ + _)
    val previousCount = state.getOrElse(0)
    Some(newCount + previousCount)
}

val totalUserreqs = userreqs.updateStateByKey(updateCount)
```

Compute a DStream based Sliding window, every 30 seconds, count requests by user over the last 5 minutes:


```python
val reqcountsByWindow = logs.map(line => (line.split(' ')(2), 1))
    .reduceByKeyAndWindow((x: Int, y: Int) => x + y, Minutes(5), Seconds(30))
```

Collect statistics with the StreamingListener API:


```python
// define listener
class MyListener extends StreamingListener {
  override def onReceiverStopped(...) {
    streamingContext.stop()
  }
}

// attach listener
streamingContext. addStreamingListener(new MyListener())
```

## Broadcast Variables

Read in list of items to broadcast from a local file:


```python
broadcast_file = "broadcast.txt"
broadcast_list = list(map(lambda l: l.strip(), open(broadcast_file)))
```

Broadcast the target list to all workers:


```python
broadcast_list_sc = sc.broadcast(broadcast_list)
```

Filter based on the broadcast list:


```python
log_file = "hdfs://localhost/user/logs/*"
filtered_data = sc.textFile(log_file)\
    .filter(lambda line: any(item in line for item in broadcast_list_sc.value))

filtered_data.take(10)
```

## Accumulators

Create an accumulator:


```python
txt_count = sc.accumulator(0)
```

Count the number of txt files in the RDD:


```python
my_data = sc.textFile(filePath)
my_data.foreach(lambda line: if '.txt' in line: txt_count.add(1))
```

Count the number of file types encountered:


```python
jpg_count = sc.accumulator(0)
html_count = sc.accumulator(0)
css_count = sc.accumulator(0)

def countFileType(s):
    if '.jpg' in s: jpg_count.add(1)
    elif '.html' in s: html_count.add(1)
    elif '.css' in s: css_count.add(1)

filename="hdfs://logs/*"

logs = sc.textFile(filename)
logs.foreach(lambda line: countFileType(line))

print  'File Type Totals:'
print '.css files: ', css_count.value
print '.html files: ', html_count.value
print '.jpg files: ', jpg_count.value
```
