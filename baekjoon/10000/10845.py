"""10845.py
큐
https://www.acmicpc.net/problem/10845
"""

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

que = deque()

for _ in range(N):
    order_list = list(map(str, input().rstrip().split()))
    order = order_list[0]

    if order == 'push':
        que.append(order_list[1])
    elif order == 'pop':
        if len(que) == 0:
            print('-1\n')
        else:
            print(f'{que.popleft()}\n')
    elif order == 'size':
        print(f'{len(que)}\n')
    elif order == 'empty':
        if len(que) == 0:
            print('1\n')
        else:
            print('0\n')
    elif order == 'front':
        if len(que) == 0:
            print('-1\n')
        else:
            print(f'{que[0]}\n')
    elif order == 'back':
        if len(que) == 0:
            print('-1\n')
        else:
            print(f'{que[-1]}\n')
