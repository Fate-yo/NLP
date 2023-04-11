# -*- coding: utf-8 -*-
import jieba
import nltk
from matplotlib import pyplot as plt
from nltk.probability import FreqDist
import matplotlib as mpl

with open("三体.txt", "r", encoding="utf-8") as f:
    str = f.read()
    print("叶文洁", str.count("叶文洁"))
    print("罗辑", str.count("罗辑"))
    print("史强", str.count("史强"))
    print("汪淼", str.count("汪淼"))
    print(str[1222:1300])
    fdist = FreqDist(str)
    print(fdist.most_common(30))
    print(len(str))
    x = jieba.lcut(str)
    text = nltk.Text(x)
    text.concordance(word="叶文洁", width=30, lines=3)
    text.similar(word='汪淼', num=10)
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    words = ['叶文洁', '罗辑', '汪淼', '史强']
    nltk.draw.dispersion.dispersion_plot(text, words, title='词汇离散图')
    plt.show()
