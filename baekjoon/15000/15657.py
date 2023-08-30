"""15657
N과 M (8)
https://www.acmicpc.net/problem/15657
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write


def sequence(num_list, result, M):
    if len(result) == M:
        print(" ".join(map(str, result)) + "\n")
        return

    for i in range(len(num_list)):
        if len(result) == 0:
            result.append(num_list[i])
            sequence(num_list, result, M)
            result.pop()

        else:
            if result[-1] <= num_list[i]:
                result.append(num_list[i])
                sequence(num_list, result, M)
                result.pop()


N, M = map(int, input().split())
num_list = sorted(list(map(int, input().split())))

sequence(num_list, list(), M)
