"""2738.py
행렬 덧셈
https://www.acmicpc.net/problem/2738
"""

N, M = map(int,input().split())
matrix = [[0 for _ in range(M)] for _ in range(N)]


for i in range(N):
    lines = list(map(int, input().split()))
    matrix[i] = [a+b for a,b in zip(matrix[i], lines)]

for i in range(N):
    lines = list(map(int, input().split()))
    matrix[i] = [a+b for a,b in zip(matrix[i], lines)]

for line in matrix:
    print(*line, sep=' ')
