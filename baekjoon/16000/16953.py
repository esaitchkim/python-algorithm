"""16953.py
A → B
https://www.acmicpc.net/problem/16953
"""

from collections import deque

A, B = map(int, input().split())
res = -1

que = deque()
que.append([A])
cnt = 0
while len(que):
    cnt += 1
    node_list = que.popleft()
    next_list = []
    for num in node_list:
        if num == B:
            res = cnt
            break
        else:
            next_num_1 = num * 2
            next_num_2 = num * 10 + 1
            if next_num_1 <= B:
                next_list.append(next_num_1)
            if next_num_2 <= B:
                next_list.append(next_num_2)
    if len(next_list):
        que.append(next_list)

print(res)
