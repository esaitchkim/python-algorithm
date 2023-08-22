"""1041.py
주사위
https://www.acmicpc.net/problem/1041
"""

"""
N * N * N 주사위에서 밖에 보이는 주사위 수 5*N*N - 8*N + 4
면 3개 보이는 주사위 = 4
면 2개 보이는 주사위 = 8*N - 12
면 1개 보이는 주사위 = 5*N*N - 16N + 12

"""

N = int(input())
A, B, C, D, E, F = map(int, input().split())
min_3 = min(A+B+C, A+B+D, A+C+E, A+D+E, B+C+F, B+D+F, C+E+F, D+E+F)
min_2 = min(A+B, A+C, A+D, A+E, B+C, B+D, B+F, C+E, C+F, D+E, D+F, E+F)
min_1 = min(A, B, C, D, E, F)

if N == 1:
    res = sum([A, B, C, D, E, F]) - max([A, B, C, D, E, F])
else:
    res = (min_3 * 4) + (min_2 * (8 * N - 12)) + (min_1 * ((5*N*N) - (16*N) + 12))
print(res)