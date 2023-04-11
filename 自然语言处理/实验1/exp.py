import jieba
import nltk
from collections import Counter

from matplotlib import pyplot as plt
from nltk.corpus import PlaintextCorpusReader
from nltk.probability import FreqDist
import re
import matplotlib as mpl
corpus_root = 'data'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
print(wordlists.fileids())
with open('.//data//金庸-射雕英雄传.txt', 'r') as f:
    str = f.read()

    print("雕：", str.count('雕'))
    print("全真派", str.count('全真派'))
    print('段天德', str.count('段天德'))
    x = jieba.lcut(str)
    fdist = FreqDist(x)



    cleaned_data = ''.join(re.findall('[\u4e00-\u9fa5]', str))
    wordlist = jieba.lcut(cleaned_data)
    text = nltk.Text(wordlist)

    mpl.rcParams['font.sans-serif'] = ['SimHei']
    words = ['全真派', '段天德', '雕', '梅超风']
    nltk.draw.dispersion.dispersion_plot(text, words, title='词汇离散图')
    plt.show()