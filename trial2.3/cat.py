import sys

argvs = sys.argv
argc = len(argvs)

print( "The content of %s ...n" % argvs[1])
f = open(argvs[1], "r")
line = f.readline()
while line:
    print( line )
    line = f.readline()
f.close
