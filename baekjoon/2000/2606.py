"""2606
바이러스
https://www.acmicpc.net/problem/2606
"""


def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += graph[node] - set(visited)
    return visited


computers = int(input())
pairs = int(input())
computer_dict = {i: set() for i in range(1, computers+1)}

for _ in range(pairs):
    a, b = map(int, input().split())
    computer_dict[a].add(b)
    computer_dict[b].add(a)


visited = dfs(computer_dict, 1)
print(len(visited)-1)
