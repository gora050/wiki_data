from pyspark.sql.types import StructType, StructField, IntegerType, FloatType, TimestampType, ArrayType, LongType, \
    StringType, DateType, BooleanType, ByteType

meta_schema = [StructField("uri", StringType()),
               StructField("request_id", StringType()),
               StructField("id", StringType()),
               StructField("dt", TimestampType()),
               StructField("domain", StringType()),
               StructField("stream", StringType()),
               StructField("topic", StringType()),
               StructField("partition", IntegerType()),
               StructField("offset", LongType())]

performer_schema = [StructField("user_text", StringType()),
                    StructField("user_groups", ArrayType(StringType())),
                    StructField("user_is_bot", BooleanType()),
                    StructField("user_id", IntegerType()),
                    StructField("user_registration_dt", TimestampType()),
                    StructField("user_edit_count", IntegerType())]

data_schema = [StructField("$schema", StringType()),
               StructField("meta", StructType(meta_schema)),
               StructField("database", StringType()),
               StructField("page_id", LongType()),
               StructField("page_title", StringType()),
               StructField("page_namespace", IntegerType()),
               StructField("rev_id", LongType()),
               StructField("rev_timestamp", TimestampType()),
               StructField("rev_sha1", StringType()),
               StructField("rev_minor_edit", BooleanType()),
               StructField("rev_len", IntegerType()),
               StructField("rev_content_format", StringType()),
               StructField("rev_content_model", StringType()),
               StructField("performer", StructType(performer_schema)),
               StructField("page_is_redirect", BooleanType()),
               StructField("comment", StringType()),
               StructField("parsedcomment", StringType())]

MAIN_SCHEMA = StructType([StructField("data", StructType(data_schema))])
