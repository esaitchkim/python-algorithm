"""1389.py
케빈 베이컨의 6단계 법칙
https://www.acmicpc.net/problem/1389
"""

import sys
from collections import deque, defaultdict
input = sys.stdin.readline
print = sys.stdout.write


def bfs(kb_graph, person, n):
    kb_values = [0] * (n+1)
    visited = [False] * (n+1)
    que = deque()
    que.append(person)
    visited[person] = True

    while len(que) > 0:
        node = que.popleft()
        p_list = kb_graph[node]
        for p in p_list:
            if not visited[p]:
                kb_values[p] = kb_values[node] + 1
                visited[p] = True
                que.append(p)
    return sum(kb_values)


N, M = map(int, input().split())

kb_graph = defaultdict(list)

for _ in range(M):
    A, B = map(int, input().split())
    kb_graph[A].append(B)
    kb_graph[B].append(A)

min_kb_value = 6 * N + 1
min_kb_person = 0
for i in range(1, N+1):
    kb_value = bfs(kb_graph, i, N)
    if min_kb_value > kb_value:
        min_kb_value = kb_value
        min_kb_person = i

print(str(min_kb_person)+'\n')
