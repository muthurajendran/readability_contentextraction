import sys,json,os,re,time
from bs4 import BeautifulSoup
sys.path.insert(0, '/Users/Muthu/Sites/isi/readability_code/python_readability')
from readability1.readability import Document
from pprint import pprint
import urllib

input_json_path = "./input/gt_data.json"


json_data = {}

with open(input_json_path) as data_file:    
    input_data = json.load(data_file)

for data in input_data:
	op_json = {}
	html = urllib.urlopen(data['id']).read()
	readable_article = Document(html).summary(True)
	writable_tag_data = readable_article.encode('utf-8')

	#Save processed html files
	f = open('./data_op_readability/file'+str(data['uid'])+".html",'w')
	f.write(writable_tag_data) 
	f.close()

	#get pure content
	doc = BeautifulSoup(writable_tag_data,'lxml')
	full_text = doc.get_text().encode('utf-8')
	processed_data = re.sub( '\s+', ' ', full_text).strip()
	op_json['id'],op_json['uid'],op_json['content'] = data['id'],data['uid'],processed_data
	json_data[data['uid']] = op_json

with open('./output_readability_txt/processed_data_readability_'+str(int(time.time()))+'.json', 'w') as outfile:
    json.dump(json_data, outfile)

print "Successfully extracted "+str(len(input_data)) + " files"


