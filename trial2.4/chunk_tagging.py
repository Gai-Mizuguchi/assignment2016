import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaChunkTagger

tagger = SennaChunkTagger('/usr/share/senna-v2.0')

argv = sys.argv
f = open(argv[1], 'r').read()
sentences = sent_tokenize(f)

word = word_tokenize(sentences[0])

chunk_list = []
chunk = tagger.tag(word)

for i in range(len(chunk)):
    chunk_list.append(chunk[i][1].split('-'))

for j in range(len(chunk_list)):
    if(chunk_list[j][0] == 'O'):
        if(chunk_list[j - 1][0] != 'O'):
            print(chunk_list[j - 1][1])
            
        else:
            pass
        
    elif(j == 0 or chunk_list[j - 1][0] == 'O'):
            print(chunk[j][0], end = ' ')
    elif( j != 0):
            if(chunk_list[j][1] == chunk_list[j - 1][1]):
                print(chunk[j][0], end = ' ')
            else:
                print(chunk_list[j - 1][1] + '\n' + chunk[j][0], end = ' ')
