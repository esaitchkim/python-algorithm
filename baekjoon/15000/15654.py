"""15654.py
N과 M (5)
https://www.acmicpc.net/problem/15654
"""

import sys
print = sys.stdout.write

N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))


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
            visited[i] = False


visited = [False] * N

sequence(num_list, list(), M, visited)
