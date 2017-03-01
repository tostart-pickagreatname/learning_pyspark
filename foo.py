"""SimpleApp.py"""
from pyspark import SparkContext, SparkConf


sc = SparkContext("local", "Simple App")

# This will parallize a piece
data = [1, 2, 3, 4, 5]
distData = sc.parallelize(data) # leveraging built-in SparkContext
distData.reduce(lambda a, b: a+b) # would now operate in parallel

# we can also supply arguments to tell it how many partitions to set for a piece of data:
distDataFivePieces = sc.parallelize(data, 5)

# NOTE: slices and partitions are synonyms here.

logFile = "./README.md"  #
logData = sc.textFile(logFile).cache() # here we use the textFile method to parse something from our local file system.
# this generates a collection of lines. Any dataset operations can now be applied to it.
# NOTE: all worker nodes must have this file at the same path - think about it as an instruction that could be sent to any of them.
# support directories, compressed files, and wildcards

directorydata = "/REPLACE/WITH/SOME/DIRECTORY"
directoryData = sc.textFile(directoryData)
# can also glob using * etc.
# wholeTextFiles allows you to et (filename, content) pairs
# sequence files are also supported

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()
