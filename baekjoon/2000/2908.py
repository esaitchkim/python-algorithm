"""2908.py
상수
https://www.acmicpc.net/problem/2908
"""

A, B = input().split()
A, B = int(A[::-1]), int(B[::-1])

print(max(A,B))