from math import *

def jSimilarity(content1, content2):
	intersection_cardinality = set.intersection(*[set(content1),set(content2)])
	union_cardinality = set.union(*[set(content1),set(content2)])
	return len(intersection_cardinality)/float(len(union_cardinality))