"""11659.py
구간 합 구하기 4
https://www.acmicpc.net/problem/11659
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
sum_list = [i for i in num_list]
for i in range(1, len(num_list)):
    sum_list[i] += sum_list[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(f'{sum_list[j] - sum_list[i-1]}\n')
