"""9375.py
패션왕 신해빈
https://www.acmicpc.net/problem/9375
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for test in range(T):
    n = int(input())
    wear_dict = {}
    for _ in range(n):
        wear, wear_type = input().rstrip().split()
        if wear_dict.get(wear_type) is None:
            wear_dict[wear_type] = []
        wear_dict[wear_type].append(wear)
    res = 1
    for value in wear_dict.values():
        res *= (len(value) + 1)
    res -= 1
    print(str(res)+'\n')
