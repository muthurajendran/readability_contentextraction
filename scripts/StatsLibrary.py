from math import *

def jSimilarity(content1, content2):
	intersection_cardinality = set.intersection(*[set(content1),set(content2)])
	union_cardinality = set.union(*[set(content1),set(content2)])
	return len(intersection_cardinality)/float(len(union_cardinality))


def getAccuracyStats(actual,predicted):
	true_positive = len(set.intersection(*[set(actual),set(predicted)]))
	false_negative = len(set(actual))-true_positive
	false_positive = len(set(predicted)) - true_positive
	true_negative = 0
	data = {}
	data["Accuracy"] = (true_positive+true_negative)/float(true_positive+true_negative+false_positive+false_negative)
	data["Precision"] = true_positive/float(true_positive+false_positive)
	data["Recall"] = true_positive/float(true_positive+false_negative)
	data['Fscore'] = 2*true_positive/float(2*true_positive + false_positive+false_negative)
	return data