"""1330.py
두 수 비교하기
https://www.acmicpc.net/problem/1330
"""

A, B = map(int,input().split())
print('>' if A>B else '<' if A<B else '==')