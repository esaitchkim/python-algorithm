"""1149.py
RGB거리
https://www.acmicpc.net/problem/1149
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
house = []

for _ in range(N):
    rgb_cost = list(map(int, input().split()))
    house.append(rgb_cost)

for i in range(1, N):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])

print(f'{min(house[N-1])}\n')
