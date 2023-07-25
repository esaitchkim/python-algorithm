"""9012.py
괄호
https://www.acmicpc.net/problem/9012
"""

T = int(input())

for _ in range(T):
    ps = input()
    lens = len(ps)
    while len(ps) > 0:
        ps = ps.replace('()', '')
        after_lens = len(ps)
        if lens == after_lens:
            break
        lens = after_lens
    if len(ps) == 0:
        print('YES')
    else:
        print('NO')
