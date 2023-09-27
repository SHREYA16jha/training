# Databricks notebook source
# dbutils.fs.mount(
#   source = "wasbs://raw@saunextadls.blob.core.windows.net",
#   mount_point = "/mnt/saunextadls/raw",
#   extra_configs = {"fs.azure.account.key.saunextadls.blob.core.windows.net":"DsZWJs7JVVHZz1I7GKyclV8ejCdj0V2UkqMlgAp6QyVOw5rvrHvmVTgwcThdHUymWg7MXon65/0z+AStj4Yiug=="})

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/saunextadls/raw/json

# COMMAND ----------

df=spark.read.json("dbfs:/mnt/saunextadls/raw/json/")

# COMMAND ----------

df.display()

# COMMAND ----------

from pyspark.sql.functions import*

# COMMAND ----------

 df1=df.withColumn("ingestiondate",current_timestamp()).withColumn("path",input_file_name())

# COMMAND ----------

df1.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists json

# COMMAND ----------

df1.write.mode("overwrite").option("path","dbfs:/mnt/saunextadls/raw/output/shreya/json").saveAsTable("json.bronzejson")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from json.bronzejson

# COMMAND ----------


