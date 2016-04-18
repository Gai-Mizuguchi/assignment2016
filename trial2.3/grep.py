import sys

argvs = sys.argv
f = open(argvs[1], "r")

for line in f:
    if line.find(argvs[2]) >= 0:
        print (line)

f.close
