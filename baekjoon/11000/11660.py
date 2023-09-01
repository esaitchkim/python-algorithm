"""11660.py
구간 합 구하기 5
https://www.acmicpc.net/problem/11660
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
mat = []
dp = [[0 for _ in range(N)] for _ in range(N)]
line = list(map(int, input().split()))
dp[0][0] = line[0]
for i in range(1, N):
    dp[0][i] = dp[0][i-1] + line[i]

mat.append(line)

for i in range(1, N):
    line = list(map(int, input().split()))
    mat.append(line)
    dp[i][0] = dp[i-1][0] + line[0]
    for j in range(1, N):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + line[j] - dp[i-1][j-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = dp[x2-1][y2-1]
    if x1 >= 2:
        res -= dp[x1-2][y2-1]
    if y1 >= 2:
        res -= dp[x2-1][y1-2]
    if x1 >= 2 and y1 >= 2:
        res += dp[x1-2][y1-2]
    print(f'{res}\n')
