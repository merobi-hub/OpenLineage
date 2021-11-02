import os

os.makedirs("/tmp/ctas_load", exist_ok=True)

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("Open Lineage Integration CTAS Load") \
    .config("spark.sql.warehouse.dir", "/tmp/ctas_load") \
    .enableHiveSupport() \
    .getOrCreate()
spark.sparkContext.setLogLevel('info')

df = spark.createDataFrame([
    {'a': 1, 'b': 2},
    {'a': 3, 'b': 4}
])

df.createOrReplaceTempView('temp')

spark.sql("CREATE TABLE tbl USING hive LOCATION '/tmp/ctas_load' AS SELECT a, b FROM temp")

# TODO: Does not generate event since it does not fire SparkListenerJobEnd
# spark.sql(f"LOAD DATA INPATH '/test_data/test_data.csv' INTO TABLE tbl")