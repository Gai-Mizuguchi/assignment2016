import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaTagger
tagger = SennaTagger('/usr/share/senna-v2.0')

argvs = sys.argv

f = open (argvs[1], "r").read()

sent_tokenize = sent_tokenize(f)
word_tokenize = word_tokenize(sent_tokenize[0])

for w,t in tagger.tag(word_tokenize):
    print(w, t)

    
