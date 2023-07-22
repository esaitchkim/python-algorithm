"""25304.py
영수증
https://www.acmicpc.net/problem/25304
"""

X = int(input())
N = int(input())

total_price = 0
for _ in range(N):
    a, b = map(int,input().split())
    total_price += (a*b)

print('Yes') if total_price==X else print('No')