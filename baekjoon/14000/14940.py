"""14940.py
쉬운 최단거리
https://www.acmicpc.net/problem/14940
"""

import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
maps = []
visited = []
destination = None
for i in range(n):
    line = list(map(int, input().split()))
    maps.append(line)
    if 2 in line:
        destination = (i, line.index(2))
    visited.append([True if v == 0 else False for v in line])

queue = deque()
queue.append([(destination[0], destination[1])])
visited[destination[0]][destination[1]] = True
maps[destination[0]][destination[1]] = 0
cnt = 1
while len(queue):
    pos_list = queue.popleft()
    next_list = []
    for i, j in pos_list:
        if 0 < i:
            if not visited[i-1][j]:
                next_list.append((i-1, j))
                visited[i-1][j] = True
                maps[i-1][j] = cnt
        if i < n-1:
            if not visited[i+1][j]:
                next_list.append((i+1, j))
                visited[i+1][j] = True
                maps[i+1][j] = cnt
        if 0 < j:
            if not visited[i][j-1]:
                next_list.append((i, j-1))
                visited[i][j-1] = True
                maps[i][j-1] = cnt
        if j < m-1:
            if not visited[i][j+1]:
                next_list.append((i, j+1))
                visited[i][j+1] = True
                maps[i][j+1] = cnt
    cnt += 1
    if len(next_list):
        queue.append(next_list)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            maps[i][j] = -1

for line in maps:
    output = ' '.join(map(str, line))
    print(output+'\n')
