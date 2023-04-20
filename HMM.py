import numpy as np


# 初始概率矩阵，状态转移矩阵，发射状态矩阵，观测序列
def viterbi_func(pi, transition_probability, emission_probability, obs_seq):
    # 将对应的数据转换为矩阵形式
    transition_probability = np.array(transition_probability)
    emission_probability = np.array(emission_probability)
    pi = np.array(pi)
    Row = transition_probability.shape[0]
    Col = len(obs_seq)

    # 定义结果矩阵
    result_probability = np.zeros((Row, Col))

    # 计算初始概率 δ1 = pi * emission_probability
    result_probability[:, 0] = pi * emission_probability[:, obs_seq[0]]

    # 计算递推公式 δt(s,c,r) = max(δt-1(s,c,r) * At-1,t) * b(s,c,r),(obs_seq[t])
    #                 i                                      i
    for t in range(1, Col):
        list_max = []
        for n in range(Row):
            # max(δt-1(s,c,r) * At-1,t)
            list_x = result_probability[:, t - 1] * transition_probability[:, n]

            # 获取最大概率
            list_p = [i * 10000 for i in list_x]

            list_max.append((max(list_p) / 10000) * emission_probability[n, obs_seq[t]])
        result_probability[:, t] = list_max
    return result_probability


pi = [0.63, 0.17, 0.2]
A = [
    [0.5, 0.375, 0.125],
    [0.25, 0.125, 0.625],
    [0.25, 0.375, 0.375]
]
B = [
    [0.6, 0.2, 0.15, 0.05],
    [0.25, 0.25, 0.25, 0.25],
    [0.05, 0.1, 0.35, 0.5]
]
obs_seq = [0, 2, 3]

ans = viterbi_func(pi, A, B, obs_seq)
print(ans)
