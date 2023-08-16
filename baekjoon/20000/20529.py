"""20529.py
가장 가까운 세 사람의 심리적 거리
https://www.acmicpc.net/problem/20529
"""

import sys
from collections import Counter

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    N = int(input())
    mbti_count = Counter([mbti for mbti in input().rstrip().split(' ')])
    mbti_count = sorted(mbti_count.items(), key=lambda x: x[1], reverse=True)
    key_len = len(mbti_count)
    res = 12
    if mbti_count[0][1] >= 3:
        res = 0
    else:
        for i in range(key_len):
            mbti_1 = mbti_count[i]
            cnt = mbti_1[1]
            for j in range(i+1, key_len):
                tmp_res = 0
                mbti_2 = mbti_count[j]
                for idx in range(4):
                    if mbti_1[0][idx] != mbti_2[0][idx]:
                        tmp_res += 1
                if cnt == 2:
                    res = min(tmp_res * 2, res)
                    continue
                for k in range(j+1, key_len):
                    mbti_3 = mbti_count[k]
                    tmp_res2 = 0
                    for idx in range(4):
                        if mbti_1[0][idx] != mbti_3[0][idx]:
                            tmp_res2 += 1
                        if mbti_2[0][idx] != mbti_3[0][idx]:
                            tmp_res2 += 1
                    res = min(res, tmp_res+tmp_res2)
    print(f'{res}\n')
