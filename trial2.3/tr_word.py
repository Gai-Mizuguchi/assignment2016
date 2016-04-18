import sys

argvs = sys.argv

f = open(argvs[1], "r")

for line in f:
    line = line.split()
    line = "\n".join(line)
    line = line.strip()

    print (line + "\n")

f.close
