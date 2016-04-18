import sys
from nltk.tokenize import sent_tokenize, word_tokenize

argvs = sys.argv

f = open(argvs[1], "r")
data = f.read()
sent_tokenize  = sent_tokenize(data)

word_tokenize_list = []
for sent in sent_tokenize:
    word_tokenize_list.extend(word_tokenize(sent))

print (word_tokenize_list)

f.close()
