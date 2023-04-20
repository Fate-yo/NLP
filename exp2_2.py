import jieba


def word_extract():
    corpus = []
    path = 'exp2/data/news.txt'
    content = ''
    for line in open(path, 'r', encoding=' gbk', errors='ignore'):
        line = line.strip()
        content += line
        corpus.append(content)
        # 加载停用词
    stop_words = []
    path = 'exp2/data/stopword.txt'
    for line in open(path, encoding='utf8'):
        line = line.strip()
        stop_words.append(line)
    split_words = []
    word_list = jieba.cut(corpus[0])
    for word in word_list:
        if word not in stop_words:
            split_words.append(word)

    dic = {}
    word_num = 10
    for word in split_words:
        dic[word] = dic.get(word, 0) + 1
    freq_word = sorted(dic.items(), key=lambda x: x[1], reverse=True)[: word_num]
    print('样本:' + corpus[0])
    print('样本分词效果: ' + '/ '.join(split_words))
    print('样本前10个高频词:' + str(freq_word))


word_extract()
