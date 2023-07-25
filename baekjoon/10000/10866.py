"""10866.py
덱
https://www.acmicpc.net/problem/10866
"""

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())

deq = deque()

for _ in range(N):
    order_list = list(map(str, input().rstrip().split()))
    order = order_list[0]
    if order == 'push_front':
        deq.appendleft(order_list[1])
    elif order == 'push_back':
        deq.append(order_list[1])
    elif order == 'pop_front':
        if len(deq) == 0:
            print('-1\n')
        else:
            print(f'{deq.popleft()}\n')
    elif order == 'pop_back':
        if len(deq) == 0:
            print('-1\n')
        else:
            print(f'{deq.pop()}\n')
    elif order == 'size':
        print(f'{len(deq)}\n')
    elif order == 'empty':
        if len(deq) == 0:
            print('1\n')
        else:
            print('0\n')
    elif order == 'front':
        if len(deq) == 0:
            print('-1\n')
        else:
            print(f'{deq[0]}\n')
    elif order == 'back':
        if len(deq) == 0:
            print('-1\n')
        else:
            print(f'{deq[-1]}\n')
