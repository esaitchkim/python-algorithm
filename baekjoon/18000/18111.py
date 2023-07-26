"""18111.py
마인크래프트
https://www.acmicpc.net/problem/18111
"""

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = {}
total_block = B

for _ in range(N):
    line = list(map(int, input().rstrip().split()))
    for i in line:
        if land.get(i) is None:
            land[i] = 1
        else:
            land[i] += 1
        total_block += i

max_height = max(land.keys())
min_height = min(land.keys())
min_sec = 2*N*M*max_height+1
max_height = min(total_block//(N*M), max_height)
res_height = 0

for h in range(max_height, min_height-1, -1):
    work_sec = 0
    for i in land.keys():
        if i > h:
            work_sec += (i-h)*2*land[i]
        else:
            work_sec += (h-i)*land[i]
    if work_sec < min_sec:
        min_sec = work_sec
        res_height = h
    if min_sec == 0:
        break

print(min_sec, res_height, sep=' ')
