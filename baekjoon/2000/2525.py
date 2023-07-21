"""2525.py
오븐 시계
https://www.acmicpc.net/problem/2525
"""

A, B = map(int,input().split())
C = int(input())

B += C

A += (B//60)
B%=60
A%=24

print(A,B,sep=' ')