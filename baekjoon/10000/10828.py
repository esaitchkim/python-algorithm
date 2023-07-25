"""10828.py
스택
https://www.acmicpc.net/problem/10828
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
stack = []
for _ in range(N):
    order_list = list(map(str, input().split()))
    if order_list[0] == 'push':
        stack.append(order_list[1])
    elif order_list[0] == 'pop':
        if len(stack) == 0:
            print('-1\n')
        else:
            print(f'{stack.pop()}\n')
    elif order_list[0] == 'size':
        print(str(len(stack))+'\n')
    elif order_list[0] == 'empty':
        if len(stack) == 0:
            print('1\n')
        else:
            print('0\n')
    else:
        if len(stack) == 0:
            print('-1\n')
        else:
            print(f'{stack[-1]}\n')
