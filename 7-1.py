from gensim.corpora import WikiCorpus
import os
import jieba
import gensim
from zhtools.langconv import Converter
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def reduce_zh():
    space = ""
    i = 0
    l = []
    zh_name = ""
    f = open()
    wkc = WikiCorpus(zh_name, lemmatize=False, dictionary={})
    for text in wkc.get_texts():
        for temp_sentence in text:
            temp_sentence = Converter("zh-hans").convert(temp_sentence)
            seg_list = list(jieba.cut(temp_sentence))
            for temp_term in seg_list:
                l.append(temp_term)
        f.write(space.join(l) + '\n')
        l = []
        i += 1
        if (i % 200 == 0):
            print("Saved" + str(i) + 'articles')
    f.close()
