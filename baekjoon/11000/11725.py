"""11725.py
트리의 부모 찾기
https://www.acmicpc.net/source/65786916
"""

import sys
from collections import deque, defaultdict

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

tree = defaultdict(list)
queue = deque()
queue.append(1)

result = [0] * (N + 1)

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

while queue:
    node = queue.popleft()
    for v in tree[node]:
        if result[v] == 0:
            result[v] = node
            queue.append(v)

for element in result[2:]:
    print(f'{element}\n')
