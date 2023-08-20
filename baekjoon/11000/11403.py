"""11403.py
경로 찾기
https://www.acmicpc.net/problem/11403
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

G = []

N = int(input())

for i in range(N):
    G.append(list(input().rstrip().split()))

for m in range(N):
    for s in range(N):
        for e in range(N):
            if G[s][m] == G[m][e] == '1':
                G[s][e] = '1'

for g in G:
    print(' '.join(g) + '\n')
