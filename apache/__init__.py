# apache
from forest._importable import LazyImport


pyspark = LazyImport("import pyspark", "PACKAGE pyspark — Python API for Apache Spark, derived from 'import pyspark', from https://github.com/apache/spark/tree/master/python, Documentation: https://spark.apache.org/docs/latest/api/python/pyspark.html")
spark = LazyImport("import pyspark as spark", "PACKAGE spark derived from pyspark — Python API for Apache Spark, derived from 'import pyspark as spark', from https://github.com/apache/spark/tree/master/python, Documentation: https://spark.apache.org/docs/latest/api/python/pyspark.html")
SparkContext = LazyImport("from pyspark import SparkContext", "CLASS pyspark.SparkContext — Main entry point for Spark functionality, derived from 'from pyspark import SparkContext', from https://github.com/apache/spark/tree/master/python, Documentation: https://spark.apache.org/docs/latest/api/python/pyspark.html#pyspark.SparkContext")

