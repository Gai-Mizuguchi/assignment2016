import sys
from nltk.tokenize import sent_tokenize, word_tokenize

argv = sys.argv

f = open(argv[1], "r").read()
sentences = sent_tokenize(f)

word_count = {}
for i in range(len(sentences)):
    for word in word_tokenize(sentences[i]):
        if word in word_count:
            word_count[word]=word_count[word] + 1
        else:
            word_count[word] = 1


for k,v in sorted(word_count.items(), key = lambda x:x[1], reverse = True):

    print(k, v)




