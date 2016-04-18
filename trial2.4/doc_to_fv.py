import sys
import shelve
from nltk.tokenize import sent_tokenize, word_tokenize

argv = sys.argv

f = open(argv[1], "r").read()
sentences = sent_tokenize(f)

word_count = {}
word_index = {}
bow_vector = {}

j = 1

for i in range(len(sentences)):
    for word in word_tokenize(sentences[i]):
        if word in word_count:
            word_count[word]=word_count[word] + 1
        else:
            word_count[word] = 1
        
        if word not in word_index:
            word_index[word] = j
            j = j + 1
        
        
dic = shelve.open('shelve_test')
dic.update(word_index)

#for k,v in sorted(word_count.items(), key = lambda x:x[1], reverse = True):

 #   print(k, v)

for index in word_index:
    bow_vector[dic[index]]=word_count[index]

dic.close()

for index in bow_vector:
    word = str(index) + ":" + str(bow_vector[index])
    print(word, end = " ")

print("")
