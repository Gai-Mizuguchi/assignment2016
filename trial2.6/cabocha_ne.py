import CaboCha

c = CaboCha.Parser("-n2")

sentence = "豊工に行っています。"

tree = c.parse(sentence)

for i in range(tree.token_size()):
    token = tree.token(i)
    if token.ne is not "O":
        print(token.surface, token.ne)
