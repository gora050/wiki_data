import pyspark
from pyspark import SparkContext
from pyspark.streaming.kafka import KafkaUtils
from schema import MAIN_SCHEMA
from pyspark.sql.types import StringType
import pyspark.sql.functions as F
from pyspark.sql.window import Window
import sys


# sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)


class Report:
    def __init__(self, topic, spark_ip="local[2]", kafka_ip="localhost:9092"):
        self.topic = topic
        self.kafka_ip = kafka_ip
        sc = SparkContext(spark_ip, appName="WikiStream")
        self.spark = pyspark.SQLContext(sc)
        self.df = self.spark \
            .read \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_ip) \
            .option("subscribe", self.topic) \
            .option("startingOffsets", "earliest") \
            .load()

    def processing_start(self):
        domain_name = Window.partitionBy("meta.domain")
        events = self.df.withColumn("value", F.col("value").cast(StringType())) \
            .withColumn("value", F.from_json("value", MAIN_SCHEMA)) \
            .select("value.data.*") \
            .withColumn("time", F.col("meta.dt").cast("timestamp"))

        domain_count = events.withColumn("domain_number", F.count("meta.domain").over(domain_name)) \
            .withColumn("domain", F.col("meta.domain")) \
            .withColumn("domain_count", F.to_json(F.struct("domain", "domain_number"))) \
            .withColumn("time", F.col("meta.dt").cast("timestamp")) \
            .dropDuplicates(["domain"]) \
            .withWatermark("time", "30 seconds") \
            .groupBy(F.window("time", "1 hour")) \
            .agg(F.collect_list("domain_count").alias("statistics")) \
            .select(F.hour("window.start").alias("time_start"),
                    F.hour("window.end").alias("time_end"),
                    "statistics")

        bots_created = events \
            .where(F.col("performer.user_is_bot") == True) \
            .withColumn("created_by_bots", F.count("meta.domain").over(domain_name)) \
            .withColumn("domain", F.col("meta.domain")) \
            .withColumn("domain_count", F.to_json(F.struct("domain", "created_by_bots"))) \
            .withColumn("time", F.col("meta.dt").cast("timestamp")) \
            .dropDuplicates(["domain"]) \
            .withWatermark("time", "30 seconds") \
            .groupBy(F.window("time", "1 hour")) \
            .agg(F.collect_list("domain_count").alias("statistics")) \
            .select(F.hour("window.start").alias("time_start"),
                    F.hour("window.end").alias("time_end"),
                    "statistics")

        domain_count.show(10, vertical=True, truncate=False)
        bots_created.show(10, vertical=True, truncate=False)


if __name__ == "__main__":
    r = Report("events")
    r.processing_start()
