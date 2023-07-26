"""1874.py
스택 수열
https://www.acmicpc.net/problem/1874
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
stack_op = []
stack = []
num = 1
flag = True
for _ in range(n):
    input_num = int(input())
    if not flag:
        continue
    while True:
        if num < input_num:
            stack.append(num)
            stack_op.append('+')
            num += 1
        elif num == input_num:
            stack_op.append('+')
            stack_op.append('-')
            num += 1
            break
        else:  # num > input_num
            pop_num = stack.pop()
            stack_op.append('-')
            if pop_num == input_num:
                break
            else:
                flag = False
                break

if flag:
    for op in stack_op:
        print(op+'\n')
else:
    print('NO\n')
