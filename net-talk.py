# from nltk.corpus import webtext
#
# for fileid in webtext.fileids():
#     # print(fileid, webtext.raw(fileid))
#
#     # 统计webtext中的每一篇文本长度和单词长度、句子长度
#     print(len(webtext.raw(fileid)),len(webtext.words(fileid)),len(webtext.sents(fileid)))
import nltk
from nltk.corpus import brown

'science_fiction'
# print(brown.categories())
# print(len(brown.sents(categories='news')))
# exit()
# for fileid in brown.fileids():
#     print(fileid)
#
new_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in new_text])
m = ['china', 'american']

for i in m:
    print(i, fdist[i])
