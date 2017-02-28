"""SimpleApp.py"""
from pyspark import SparkContext, SparkConf

# This will parallize a piece
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data) # leveraging built-in SparkContext
distData.reduce(lambda a, b: a+b) # would now operate in parallel

# we can also supply arguments to tell it how many partitions to set for a piece of data:
distDataFivePieces = sc.parallelize(data, 5)

# NOTE: slices and partitions are synonyms here.

logFile = "./README.md"  # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()
