"""2178.py
미로 탐색
https://www.acmicpc.net/problem/2178
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []
visited = []
for i in range(N):
    lines = list(input().rstrip())
    line_visited = [False if j == '1' else True for j in lines]
    maze.append(lines)
    visited.append(line_visited)
N -= 1
M -= 1

queue = deque()
queue.append([(0, 0)])
visited[0][0] = True
cnt = 0
while len(queue) > 0:
    pos_list = queue.popleft()
    next_list = []
    cnt += 1
    if (N, M) in pos_list:
        break
    for i, j in pos_list:
        if i > 0 and not visited[i-1][j]:
            next_list.append((i-1, j))
            visited[i-1][j] = True
        if i < N and not visited[i+1][j]:
            next_list.append((i+1, j))
            visited[i+1][j] = True
        if j > 0 and not visited[i][j-1]:
            next_list.append((i, j-1))
            visited[i][j-1] = True
        if j < M and not visited[i][j+1]:
            next_list.append((i, j+1))
            visited[i][j+1] = True
    if len(next_list) > 0:
        queue.append(next_list)

print(cnt)
