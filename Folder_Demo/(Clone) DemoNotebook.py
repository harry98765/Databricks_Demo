# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello World"

# COMMAND ----------

# MAGIC %md
# MAGIC #Title
# MAGIC ##Title1

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.jobs.help()

# COMMAND ----------

files=dbutils.fs.ls('/databricks-datasets/')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------


