"""10869.py
사칙연산
https://www.acmicpc.net/problem/10869
"""

A, B = map(int, input().split())
print(*[A+B,A-B,A*B,A//B,A%B], sep="\n")