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
