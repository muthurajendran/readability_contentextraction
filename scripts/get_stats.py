###############################
# File has script that will generate the similarity between the gold data 
# and processed data from the content extraction algorithms
###############################

from jaccard_similarity import jSimilarity
import sys,json

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

for gold in gold_data:
	try:
		processed_data_item = processed_data[str(gold['uid'])]
		jacc_sim = jSimilarity(gold['required'] + gold['optional'],processed_data_item['content'])
		print gold['uid'], jacc_sim, gold['id']
		# print gold['required'] + gold['optional']
		# print "*"*50
		# print processed_data_item['content']
		# print "*"*50
	except Exception, e:
		print "No id found with num "+ str(gold['uid']) +"! Skipping"


