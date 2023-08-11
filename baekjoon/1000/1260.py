"""1260.py
DFS와 BFS
https://www.acmicpc.net/problem/1260
"""

import sys
from collections import deque, defaultdict
input = sys.stdin.readline
print = sys.stdout.write


def bfs(graph, root, N):
    queue = deque([root])
    visited = [False] * (N+1)
    visited[root] = True
    res = []
    while queue:
        v = queue.popleft()
        res.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return res


def dfs(graph, root, N):
    stack = [root]
    visited = [False] * (N+1)
    res = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            res.append(v)
            stack.extend(reversed(graph[v]))
            visited[v] = True

    return res


N, M, V = map(int, input().split())
graph = defaultdict(list)

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)
for key in graph.keys():
    graph[key] = sorted(graph[key])

res_bfs = bfs(graph, V, N)
res_dfs = dfs(graph, V, N)
res_dfs = ' '.join([str(i) for i in res_dfs])
res_bfs = ' '.join([str(i) for i in res_bfs])

print(res_dfs+'\n')
print(res_bfs+'\n')
