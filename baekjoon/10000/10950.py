"""10950.py
A+B - 3
https://www.acmicpc.net/problem/10950
"""

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)