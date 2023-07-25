"""24267.py
알고리즘 수업 - 알고리즘의 수행 시간 6
https://www.acmicpc.net/problem/24267
"""

# 사면체수 1, 4, 10, 20, 35, ...
# n=1부터 계산 시 (n-2) * (n - 1) * n // 6
n = int(input())
print((n-2)*(n-1)*n//6)
print(3)
