import MeCab

mecab = MeCab.Tagger ("mecabrc")

sent = "豊工に行ってます。"

print(mecab.parse(sent))


