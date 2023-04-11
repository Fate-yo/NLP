from nltk.book import *
import matplotlib.pyplot as plt
#
# fdist = FreqDist(text1)
# print(text1)
# plt.rcParams['font.sans-serif'] = ['SimHei']
# # import nltk
# #
# # nltk.draw.dispersion.dispersion_plot(text1, ['hey', 'apple', 'Moby', 'danger'], title='词汇分布情况的离散图')
# # plt.show()
#
# plt.grid()
# fdist1 = dict(fdist)
# fdist1 = sorted(fdist1.items(), key=lambda x: x[1], reverse=True)
# x = []
# y = []
#
# for i in range(10):
#     x.append(fdist1[i][0])
#     y.append(fdist1[i][1])
#
# t = 0
# for i in range(len(y)):
#     y[i] = y[i] + t
#     t = y[i]
# plt.plot(x, y)
# plt.title("词频")
# plt.ylabel('累计频率')
# plt.xlabel('常用词')
# plt.show()
# print(text1.similar("pretty"))##返回相似
# print(text1.concordance(word= "danger"))#搜索指定词
# print(text1.collocations())#函数搜索搭配词语
# print(text1.common_contexts(['mostrous','very'])) # 搜索词的共同上下文
# print(set(text1)) #获取词汇文本表
# sorted(set(text1)) #排序
# FreqDist(text1) #查询词汇频率
import re,nltk,zhconv
from urllib.request import urlopen
url='https://www.gutenberg.org/cache/epub/23962/pg23962.html'#西游记
url1='https://www.gutenberg.org/cache/epub/24264/pg24264.html'#红楼梦
url2='https://www.gutenberg.org/cache/epub/23950/pg23950.html'#三国志演义
html1=urlopen(url).read()

html1=html1.decode('utf-8')
text1 = zhconv.convert(html1, 'zh-hans')
print(text1)