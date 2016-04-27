import MeCab
import sys

mt = MeCab.Tagger("mecabrc")

for sentence in mt.parse("豊工に行っています。").split("\n"):
    i = 1
    for words in sentence.split(","):
        if i in[1,7]:
            print(words,end=" ")
        i = i+1

    print("")
