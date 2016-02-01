###############################
# File has script that will generate the similarity between the gold data 
# and processed data from the content extraction algorithms
###############################

from StatsLibrary import jSimilarity,getAccuracyStats
import sys,json
from csv import DictWriter

def write_to_excel(data_out):
	with open('results_justext_goodbad.csv','w') as outfile:
		writer = DictWriter(outfile, ('id','url','Accuracy','Precision','Recall','Fscore','Jaccard Similarity'))
		writer.writeheader()
		writer.writerows(data_out)

if len(sys.argv) < 3:
	print "Expecting 2 arguments"
	print "Usage : <script.py> <gold_data_jsonfile> <processed_data_jsonfile>"
	sys.exit()

gold_file = sys.argv[1] 
processed_file = sys.argv[2]

with open(gold_file) as data_file:    
    gold_data = json.load(data_file)

with open(processed_file) as data_file:    
    processed_data = json.load(data_file)

data_out = []
for gold in gold_data:
	try:
		processed_data_item = processed_data[str(gold['uid'])]
		ggContent = gold['required'] + gold['optional']
		temp = getAccuracyStats(ggContent,processed_data_item['content'])
		temp['Jaccard Similarity'] = jSimilarity(ggContent,processed_data_item['content'])
		temp['url'],temp['id'] = gold['id'],gold['uid']
		data_out.append(temp)
	except Exception, e:
		print "No id found with num "+ str(gold['uid']) +"! Skipping"
		raise e

if data_out:
	write_to_excel(data_out)
else:
	print "Nothing to process!! Excel file not created. Exiting"
