import sys

argvs = sys.argv
argc  = len(argvs)

f = open(argvs[1], "r")
g = open(argvs[2], "w")

for line in f:
    g.write (line)
f.close

