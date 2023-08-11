"""18870.py
좌표 압축
https://www.acmicpc.net/problem/18870
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
num_list = list(map(int, input().split()))
order_dict = {}
cnt = 0
for num in sorted(num_list):
    if order_dict.get(num) is not None:
        continue
    order_dict[num] = cnt
    cnt += 1

res = ' '.join([str(order_dict[num]) for num in num_list])
print(res + '\n')
