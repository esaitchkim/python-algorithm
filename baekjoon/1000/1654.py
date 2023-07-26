"""1654.py
랜선 자르기
https://www.acmicpc.net/problem/1654
"""

import sys

input = sys.stdin.readline

K, N = map(int, input().split())
total_cm = 0
cable_list = []
for _ in range(K):
    cable_list.append(int(input()))
max_cm = max(cable_list)
min_cm = 1
res_cm = 1

while max_cm >= min_cm:
    now_cm = (min_cm+max_cm)//2
    lan_cnt = sum(x//now_cm for x in cable_list)
    if lan_cnt >= N:
        res_cm = now_cm
        min_cm = now_cm+1
    else:
        max_cm = now_cm-1

print(res_cm)
