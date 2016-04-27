import CaboCha

c = CaboCha.Parser()

sentence = "豊工に行っています。"

print (c.parseToString(sentence))

tree = c.parse(sentence)

print (tree.toString(CaboCha.FORMAT_TREE))
print (tree.toString(CaboCha.FORMAT_LATTICE))
