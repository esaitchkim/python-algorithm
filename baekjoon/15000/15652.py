"""15652.py
N과 M (4)
https://www.acmicpc.net/problem/15652
"""

import sys
print = sys.stdout.write

N, M = map(int, input().split())


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


num_list = [i for i in range(1, N+1)]

sequence(num_list, list(), M)
