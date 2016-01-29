###############################
# File has script that will generate the similarity between the gold data 
# and processed data from the content extraction algorithms
###############################

from jaccard_similarity import jSimilarity
import sys

tst = jSimilarity("hey dude","dude")

print tst
