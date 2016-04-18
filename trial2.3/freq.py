import sys

argvs = sys.argv
argc = len(argvs)

f = open (argvs[1], "r")
data = f.read()

words = {}
for word in data.split():
    words[word] = words.get(word, 0) + 1

d = [(v,k) for k,v in words.items()]
d.sort()
d.reverse()
for count, word in d[:10]:
    print(' ' + str(count), word)

f.close()
