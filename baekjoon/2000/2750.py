"""2750.py
수 정렬하기
https://www.acmicpc.net/problem/2750
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

num_list = sorted(num_list)

for i in num_list:
    print(f'{i}\n')
