"""2579.py
계단 오르기
https://www.acmicpc.net/problem/2579
"""

n = int(input())
stairs = [int(input()) for _ in range(n)]
dp = [i for i in stairs]
if n >= 2:
    dp[1] += dp[0]
    if n >= 3:
        dp[2] += max(dp[0], stairs[1])

for i in range(3, n):
    dp[i] += max(dp[i-3]+stairs[i-1], dp[i-2])
print(dp[n-1])
