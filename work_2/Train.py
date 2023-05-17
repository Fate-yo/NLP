import os
import json
import datetime


def train():
    trans_prob = {}
    emit_prob = {}
    init_prob = {}
    Count_dict = {}
    state_list = ['B', 'M', 'E', 'S']
    for state in state_list:
        trans = {}
        for s in state_list:
            trans[s] = 0
        trans_prob[state] = trans
        emit_prob[state] = {}
        init_prob[state] = 0
        Count_dict[state] = 0
    count = -1
    path = './data/trainCorpus.txt'
    for line in open(path, 'r'):
        count += 1
        line = line.strip()
        if not line:
            continue
        word_list = []
        for i in line:
            if i != ' ':
                word_list.append(i)
        word_label = []
        for word in line.split():
            label = []
            if len(word) == 1:
                label.append('S')
            else:
                label += ['B'] + ['M'] * (len(word) - 2) + ['E']
            word_label.extend(label)
        for index, value in enumerate(word_label):
            Count_dict[value] += 1
            if index == 0:
                init_prob[value] += 1
            else:
                trans_prob[word_label[index - 1]][value] += 1
                emit_prob[word_label[index]][word_list[index]] = (
                        emit_prob[word_label[index]].get(word_list[index], 0) + 1.0
                )

    for key, value in init_prob.items():
        init_prob[key] = value * 1 / count
    for key, value in trans_prob.items():
        for k, v in value.items():
            value[k] = v / Count_dict[key]
        trans_prob[key] = value
    for key, value in emit_prob.items():
        for k, v in value.items():
            value[k] = (v + 1) / Count_dict[key]
        emit_prob[key] = value
    model = './tmp/hmm_model.json'
    f = open(model, 'w')
    f.write(json.dumps(trans_prob) + '\n' + json.dumps(emit_prob) + '\n' + json.dumps(init_prob))
    f.close()
