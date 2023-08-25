"""5430.py
AC
https://www.acmicpc.net/problem/5430
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr_str = input().rstrip().replace(' ', '')
    arr_str = arr_str[1:-1]
    arr_list = []
    if n > 0:
        arr_list = arr_str.split(',')
    start_idx = 0
    end_idx = n
    reverse_flag = False
    error_flag = False
    for op in p:
        if op == 'R':
            reverse_flag = not reverse_flag
        else:
            if start_idx >= end_idx:
                error_flag = True
                break
            if not reverse_flag:
                start_idx += 1
            else:
                end_idx -= 1

    if error_flag:
        print('error\n')
    else:
        if reverse_flag:
            print(f'[{",".join(reversed(arr_list[start_idx:end_idx]))}]\n')
        else:
            print(f'[{",".join(arr_list[start_idx:end_idx])}]\n')
