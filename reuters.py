import nltk
from nltk.corpus import reuters, inaugural
import matplotlib.pyplot as plt

#
# plt.rcParams['font.sans-serif'] = ['SimHei']
#
# # 获取路透社语料库中的所有文档
# documents = reuters.fileids()
#
# # 获取路透社语料库中的所有单词，并将它们转换为小写形式
# words = [w.lower() for w in reuters.words()]
#
# # 使用NLTK中的FreqDist函数进行词频统计，并选取前20个出现频率最高的单词
# freq_dist = nltk.FreqDist(words)
# top_words = freq_dist.most_common(20)
#
# # 输出词频统计结果
# x = []
# y = []
# other = ".-,;';[]`~1"
# for word, frequency in top_words:
#     if other.find(word) == -1:
#         x.append(word)
#         y.append(frequency)
#
# plt.figure()
# plt.xlabel('word')
# plt.ylabel('f')
# plt.plot(x, y)
# plt.show()
# print(reuters.fileids()[:5])
# print(reuters.categories('test/14832'))
# from nltk.corpus import inaugural
#
# # for fileid in inaugural.fileids():
# # print(fileid)
# # print([fileid[:4] for fileid in inaugural.fileids()])
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.grid()
models = ['citizen', 'free']
style = ['--', '-']

dic = {}
from nltk.probability import ConditionalFreqDist, FreqDist

for fileid in inaugural.fileids():
    word = inaugural.words(fileid)
    fdist = nltk.FreqDist(w.lower() for w in word)
    dic.update({fileid[:4]: [{'free': fdist[models[1]]}, {'citizen': fdist[models[0]]}]})

# print(dic)
x = [fileid[:4] for fileid in inaugural.fileids()]
y1 = []
y2 = []
for fileid in inaugural.fileids():
    y1.append(dic[fileid[:4]][0]['free'])
    y2.append(dic[fileid[:4]][1]['citizen'])

plt.plot(x,y1)
plt.plot(x,y2)
plt.show()
cfd = ConditionalFreqDist((target, fileid[:4])
                          for fileid in inaugural.fileids()
                          for w in inaugural.words(fileid)
                          for target in ['free', 'citizen']
                          if w.lower().startswith(target)
                          )



print(cfd.items())
cfd.plot()
# import nltk
# from nltk.corpus import inaugural
# from nltk.probability import ConditionalFreqDist, FreqDist
# import jieba
#
# seq1 = "张宪民副书记对学校安全工作作出部署：一是强化安全意识，不断提升风险防范能力；二是强化安全责任，切实筑牢安全防线；三是强化安全落实，定期开展隐患排查，发现问题及时整改。他强调，要将安全意识内化于心，外化于行，以时时放心不下的责任感和紧迫感抓紧抓牢安全工作，扎实推进平安校园建设。"
# seq2 = "张应辉校长对学校安全工作作出指示。他强调，要时时刻刻绷紧安全这根弦，不断增强安全意识，及时总结经验教训，真正做到防患于未然：一是坚决杜绝麻痹懈怠心理，切实抓好安全措施落实落地，全力防范化解风险隐患；二是进一步完善安全工作预案，常态化开展各项巡查工作，全力营造平安、稳定、和谐的校园环境。"
# word1 = jieba.lcut(seq1)
# word2 = jieba.lcut(seq2)
# fdist1 = FreqDist(word1)
# fdist2 = FreqDist(word2)
# b = ConditionalFreqDist()
# for word in word1:
#     b['positive'][word] += 1
#
# for word in word2:
#     b['neg'][word] += 1
# print(b.items())
# print(b['positive'].N())
# print(b.conditions())
# feel = ['pos', 'neg']
# model = ['安全', '副']
# print(b.tabulate(condations=feel, samples=model))
# b.plot()
