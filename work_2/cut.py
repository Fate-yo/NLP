import os
import json
from work_2.viterbi import viterbi


def cut(text):
    state_list = ['B', 'M', 'E', 'S']
    model = './tmp/hmm_model.json'
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
