from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()


def create_df():    
    columns = ["language","users_count"]
    data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]
    df = spark.createDataFrame(data).toDF(*columns)
    row_count = df.count()
    return row_count

def get_db_utils(spark):
    dbutils = None
    if spark.conf.get("spark.databricks.service.client.enabled") == "true":
        from pyspark.dbutils import DBUtils
        dbutils = DBUtils(spark)
    else:
        import IPython
        dbutils = IPython.get_ipython().user_ns["dbutils"]
    return dbutils


def dbutils_path():
    dbutils = get_db_utils(spark)
    print("file location")
    print(dbutils.fs.ls('abfss://dev@forgeinsightsdevstorage.dfs.core.windows.net/xsbg/ea/lab'))

def main():
    dbutils_path()
    