"""1012.py
유기농 배추
https://www.acmicpc.net/problem/1012
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for i in range(N)] for j in range(M)]
    warm = 0
    for k in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    for x in range(M):
        for y in range(N):
            v_set = set()
            if field[x][y] == 1:
                warm += 1
                v_set.add((x, y))
                field[x][y] = 0
                while len(v_set):
                    tmp_x, tmp_y = v_set.pop()
                    if 0 < tmp_x:
                        if field[tmp_x-1][tmp_y] == 1:
                            field[tmp_x-1][tmp_y] = 0
                            v_set.add((tmp_x-1, tmp_y))
                    if tmp_x < M-1:
                        if field[tmp_x+1][tmp_y] == 1:
                            field[tmp_x+1][tmp_y] = 0
                            v_set.add((tmp_x+1, tmp_y))

                    if 0 < tmp_y:
                        if field[tmp_x][tmp_y-1] == 1:
                            field[tmp_x][tmp_y-1] = 0
                            v_set.add((tmp_x, tmp_y-1))
                    if tmp_y < N-1:
                        if field[tmp_x][tmp_y+1] == 1:
                            field[tmp_x][tmp_y+1] = 0
                            v_set.add((tmp_x, tmp_y+1))

    print(f'{warm}\n')
