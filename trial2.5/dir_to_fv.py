import sys
import shelve
import os
from nltk.tokenize import sent_tokenize, word_tokenize

argv = sys.argv

files = []

print(argv[2], end=' ')

for txtlist in os.listdir(argv[1]):
    
    if txtlist.endswith(".txt"):
        files.append(txtlist)

for txtfiles in files:
        
        sentences = sent_tokenize(open(txtfiles).read())

        word_count = {}
        word_index = shelve.open('shelve_test.db')

        j = len(word_index) + 1

        for i in range(len(sentences)):
            for word in word_tokenize(sentences[i]):
                if word in word_count:
                    word_count[word]=word_count[word] + 1
                else:
                    word_count[word] = 1
        
                    if word not in word_index:
                        word_index[word] = j
                        j = j + 1

        bow_vector = [0]*len(word_index)
        for key, index in word_count.items():
            bow_vector[word_index[key] - 1]=index

        word_index.close()

        for l in range(len(bow_vector)):
            if bow_vector[l] != 0:
                word = str(l + 1) + ":" + str(bow_vector[l])
                print(word, end = " ")

        print("")
