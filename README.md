# Wiki Stream Data Processing
![alt text](https://github.com/gora050/wiki_data/blob/master/ProjectSystemDiagram.png)
## Usage Category A
1. First you need to install Kafka and Spark on your machine(steps depends on the OS which you use)
2. Start zookeeper, kafka-server and spark standalone cluster or cluster whith multiple slaves
3. Start producer which will post wiki events to kafka topic for at least 6 hours.
4. ```spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.6 src/spark_application.py```
5. Go to Flask and try following endpoints:
* user_activity/
* bots_created/
* domain_count/

##Result examples Category A
