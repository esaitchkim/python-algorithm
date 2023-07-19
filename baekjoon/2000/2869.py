"""2869.py
달팽이는 올라가고 싶다
https://www.acmicpc.net/problem/2869
"""

A, B, V = map(int,input().split())

n = (V-B)/(A-B)
int_n = int(n)
n = int_n if n==int_n else int_n+1

print(n)