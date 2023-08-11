"""11724.py
연결 요소의 개수
https://www.acmicpc.net/problem/11724
"""

import sys
input = sys.stdin.readline


def dfs(graph, root, visited):
    stack = [root]
    while stack:
        v = stack.pop()
        if not visited[v]:
            stack.extend(graph[v])
            visited[v] = True
    return visited


N, M = map(int, input().split())

graph = {i: [] for i in range(1, N+1)}
visited = [True] + [False]*N
cnt = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph.keys():
    if not visited[i]:
        visited = dfs(graph, i, visited)
        cnt += 1

print(cnt)
