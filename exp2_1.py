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
    path = './exp2/data/trainCorpus.txt'
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
    model = 'exp2/tmp/hmm_model.json'
    f = open(model, 'w')
    f.write(json.dumps(trans_prob) + '\n' + json.dumps(emit_prob) + '\n' + json.dumps(init_prob))
    f.close()


def viterbi(text, state_list, init_prob, trans_prob, emit_prob):
    V = [{}]
    path = {}
    for state in state_list:
        V[0][state] = init_prob[state] * emit_prob[state].get(text[0], 0)
        path[state] = [state]
    key_list = []
    for key, value in emit_prob.items():
        for k, v in value.items():
            key_list.append(k)

    for t in range(1, len(text)):
        V.append({})
        newpath = {}

        for state in state_list:
            if text[t] in key_list:
                emit_count = emit_prob[state].get(text[t], 0)
            else:
                emit_count = 1
            (prob, a) = max([(V[t - 1][s] * trans_prob[s].get(state, 0) * emit_count, s)
                             for s in state_list if V[t - 1][s] > 0])
            V[t][state] = prob
            newpath[state] = path[a] + [state]
        path = newpath
    if emit_prob['M'].get(text[-1], 0) > emit_prob['S'].get(text[-1], 0):
        (prob, a) = max([(V[len(text) - 1][s], s) for s in ('E', 'M',)])
    else:
        (prob, a) = max([(V[len(text) - 1][s], s) for s in state_list])
    return prob, path[a]


def cut(text):
    state_list = ['B', 'M', 'E', 'S']
    model = 'exp2/tmp/hmm_model.json'
    if os.path.exists(model):
        f = open(model, 'rb')
        trans_prob = json.loads(f.readline())
        emit_prob = json.loads(f.readline())
        init_prob = json.loads(f.readline())
        f.close()
    else:
        trans_prob = {}
        emit_prob = {}
        init_prob = {}

    prob, pos_list = viterbi(text, state_list, init_prob, trans_prob, emit_prob)
    begin, follow = 0, 0
    for index, char in enumerate(text):
        state = pos_list[index]
        if state == 'B':
            begin = index
        elif state == 'E':
            yield text[begin: index + 1]
            follow = index + 1
        elif state == 'S':
            yield char
            follow = index + 1
    if follow < len(text):
        yield text[follow:]


text = "深航客机攀枝花机场遇险：机腹轮胎均疑受损，跑道灯部分损坏"

start_time = datetime.datetime.now()
train()
end_time = datetime.datetime.now()
print((end_time - start_time).seconds)
cut(text)
print(text)
print(str(list(cut(text))))
