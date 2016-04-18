from nltk.tokenize import sent_tokenize
import sys

argvs = sys.argv

f = open(argvs[1], "r")
text = f.read()

sent_tokenize_list = sent_tokenize(text)

print(sent_tokenize_list)

f.close()

