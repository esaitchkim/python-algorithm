"""1966.py
프린터 큐
https://www.acmicpc.net/problem/1966
"""

import sys
from collections import deque, defaultdict

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    N, M = map(int, input().split())
    docs_deq = deque(map(int, input().split()))
    res_docs = docs_deq[M]
    res_cnt = 1
    pri_dict = defaultdict(int)
    for key in docs_deq:
        pri_dict[key] += 1

    while True:
        max_key = max(pri_dict.keys())
        docs = docs_deq.popleft()
        if docs == max_key:
            if M == 0:
                print(res_cnt)
                break
            else:
                pri_dict[docs] -= 1
                if pri_dict[docs] == 0:
                    del pri_dict[docs]
                M -= 1
                res_cnt += 1
        else:
            docs_deq.append(docs)

            if M == 0:
                M = len(docs_deq)-1
            else:
                M -= 1
