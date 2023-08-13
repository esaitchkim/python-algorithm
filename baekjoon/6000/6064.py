"""6064.py
카잉 달력
https://www.acmicpc.net/problem/6064
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    if x == y:
        print(f'{x}\n')
        continue
    if M > N:
        M, N = N, M
        x, y = y, x
    t_y = x
    y_list = [True]*(N+1)
    while True:
        t_y += M
        md = t_y % N
        md = N if md == 0 else md
        if y_list[md]:
            if md == y:
                print(f'{t_y}\n')
                break
            y_list[md] = False
        else:
            print(f'-1\n')
            break
