"""11723.py
집합
https://www.acmicpc.net/problem/11723
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

M = int(input())
set_list = [False] * 21

for _ in range(M):
    order_list = list(map(str, input().split()))
    operation = order_list[0]
    if len(order_list) > 1:
        order_list[1] = int(order_list[1])

    if operation == 'add':
        set_list[order_list[1]] = True
    elif operation == 'remove':
        if set_list[order_list[1]]:
            set_list[order_list[1]] = False
    elif operation == 'check':
        if set_list[order_list[1]]:
            print('1\n')
        else:
            print('0\n')
    elif operation == 'toggle':
        set_list[order_list[1]] = False if set_list[order_list[1]] else True
    elif operation == 'all':
        set_list = [True] * 21

    elif operation == 'empty':
        set_list = [False] * 21
