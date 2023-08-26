"""15650.py
N과 M (2)
https://www.acmicpc.net/problem/15650
"""

import sys
print = sys.stdout.write

N, M = map(int, input().split())


def sequence(num_list, result, M, visited):
    if len(result) == M:
        print(" ".join(map(str, result))+"\n")
        return

    for i in range(len(num_list)):
        if not visited[i]:
            visited[i] = True
            result.append(num_list[i])
            sequence(num_list, result, M, visited)
            result.pop()

            for j in range(i+1, len(visited)):
                visited[j] = False


num_list = [i for i in range(1, N+1)]
visited = [False] * N

sequence(num_list, list(), M, visited)
