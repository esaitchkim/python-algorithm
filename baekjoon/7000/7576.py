"""7576.py
토마토
https://www.acmicpc.net/problem/7576
"""

import sys
from collections import deque
input = sys.stdin.readline


def all_true(matrix):
    for row in matrix:
        for element in row:
            if not element:
                return False
    return True


def bfs(graph, root_list, visited, n, m):
    queue = deque([root_list])
    cnt = -1
    while queue:
        cnt += 1
        past_list = queue.popleft()
        present_list = []
        for x, y in past_list:
            if 0 < x and graph[x-1][y] == 0 and not visited[x-1][y]:
                present_list.append((x-1, y))
                visited[x-1][y] = True
            if x < n and graph[x+1][y] == 0 and not visited[x+1][y]:
                present_list.append((x+1, y))
                visited[x+1][y] = True
            if 0 < y and graph[x][y-1] == 0 and not visited[x][y-1]:
                present_list.append((x, y-1))
                visited[x][y-1] = True
            if y < m and graph[x][y+1] == 0 and not visited[x][y+1]:
                present_list.append((x, y+1))
                visited[x][y+1] = True
        if len(present_list):
            queue.append(present_list)

    return cnt if all_true(visited) else -1


M, N = map(int, input().split())
box = []
root_list = []
visited = []
for i in range(N):
    lines = list(map(int, input().split()))
    box.append(lines)
    line_visited = [False if element == 0 else True for element in lines]
    visited.append(line_visited)
    for j in range(M):
        if lines[j] == 1:
            root_list.append((i, j))

cnt = bfs(box, root_list, visited, N-1, M-1)
print(cnt)
