import pyspark
from pyspark import SparkContext
from pyspark.streaming.kafka import KafkaUtils
from schema import MAIN_SCHEMA
from pyspark.sql.types import StringType
import pyspark.sql.functions as F
from pyspark.sql.window import Window
import sys
from datetime import datetime, timedelta
import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

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

        self.events = self.df.withColumn("value", F.col("value").cast(StringType())) \
            .withColumn("value", F.from_json("value", MAIN_SCHEMA)) \
            .select("value.data.*") \
            .withColumn("time", F.col("meta.dt").cast("timestamp"))

    def domain_count(self):
        curr_time = datetime.now()
        six_hours = curr_time - timedelta(hours=6)
        last_hour = curr_time - timedelta(hours=1)
        domain_name = Window.partitionBy("meta.domain")

        domain_count = self.events.withColumn("domain_number", F.count("meta.domain").over(domain_name)) \
            .where((F.col("time") > six_hours) & (F.col("time") < last_hour)) \
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

        result_df = domain_count.toPandas()
        result_df = result_df.to_json(orient="records")
        return result_df

    def bots_created(self):
        curr_time = datetime.now()
        six_hours = curr_time - timedelta(hours=6)
        last_hour = curr_time - timedelta(hours=1)

        domain_name = Window.partitionBy("meta.domain")
        bots_created = self.events \
            .where(F.col("performer.user_is_bot") == True) \
            .where((F.col("time") > six_hours) & (F.col("time") < last_hour)) \
            .withColumn("created_by_bots", F.count("meta.domain").over(domain_name)) \
            .withColumn("domain", F.col("meta.domain")) \
            .withColumn("domain_count", F.to_json(F.struct("domain", "created_by_bots"))) \
            .dropDuplicates(["domain"]) \
            .withWatermark("time", "30 seconds") \
            .groupBy(F.window("time", "1 hour")) \
            .agg(F.collect_list("domain_count").alias("statistics")) \
            .select(F.hour("window.start").alias("time_start"),
                    F.hour("window.end").alias("time_end"),
                    "statistics")
        result_df = bots_created.toPandas()
        result_df = result_df.to_json(orient="records")
        return result_df

    def user_activity(self):
        curr_time = datetime.now()
        six_hours = curr_time - timedelta(hours=6)
        last_hour = curr_time - timedelta(hours=1)
        created_by = Window.partitionBy("performer.user_id")
        user_activity = self.events.withColumn("page_titles", F.collect_list("page_title").over(created_by)) \
            .where((F.col("time") > six_hours) & (F.col("time") < last_hour)) \
            .withColumn("current_time", F.current_timestamp()) \
            .withColumn("time_start", F.col("current_time") - F.expr("INTERVAL 6 HOURS")) \
            .withColumn("time_end", F.col("current_time") - F.expr("INTERVAL 1 HOURS")) \
            .withColumn("user_id", F.col("performer.user_id")) \
            .withColumn("user_name", F.col("performer.user_text")) \
            .withColumn("number_of_pages", F.size("page_titles")) \
            .dropDuplicates(["user_id"]) \
            .orderBy(F.col("number_of_pages").desc()).limit(20) \
            .select("user_id", "user_name", "number_of_pages", "page_titles", "time_start", "time_end")
        result_df = user_activity.toPandas()
        result_df = result_df.to_json(orient="records")
        return result_df


r = Report("events")


@app.route("/user_activity")
def get_user_act():
    return r.user_activity()


@app.route("/bots_created")
def get_bots_created():
    return r.bots_created()


@app.route("/domain_count")
def get_domain_count():
    return r.domain_count()


if __name__ == "__main__":
    # r = Report("events")
    app.run()
    # r.processing_start()
