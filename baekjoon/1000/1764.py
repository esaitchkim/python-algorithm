"""1764.py
듣보잡
https://www.acmicpc.net/problem/1764
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

not_heard = {input().rstrip(): True for _ in range(N)}
not_heard_and_see_list = []
for _ in range(M):
    not_see = input().rstrip()
    not_heard_and_see = not_heard.get(not_see)
    if not_heard_and_see:
        not_heard_and_see_list.append(not_see)

not_heard_and_see_list = sorted(not_heard_and_see_list)
print(f'{len(not_heard_and_see_list)}\n')
for p in not_heard_and_see_list:
    print(p+'\n')
