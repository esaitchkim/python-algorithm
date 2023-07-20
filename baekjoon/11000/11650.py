"""11650.py
좌표 정렬하기
https://www.acmicpc.net/problem/11650
"""
import sys
from collections import defaultdict

input = sys.stdin.readline
write = sys.stdout.write


N = int(input().strip())

coordinate = defaultdict(list)

for _ in range(N):
    x, y = map(int,input().strip().split())
    coordinate[x].append(y)


for x in sorted(coordinate.keys()):
    for y in sorted(coordinate[x]):
        write(f'{x} {y}\n')
