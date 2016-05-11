import sys

newLabel = ''
for Label in open('labels.txt', "r"):
    if int( Label ) >= 4:
        newLabel += '1\n'
    else:
        newLabel += '-1\n'

open(sys.argv[1], "w").write(newLabel)
