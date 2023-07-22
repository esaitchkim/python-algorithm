"""10813.py
공 바꾸기
https://www.acmicpc.net/problem/10813
"""

N, M = map(int,input().split())

basket = [i for i in range(N+1)]

for _ in range(M):
    b1, b2 = map(int,input().split())
    basket[b1], basket[b2] = basket[b2], basket[b1]

print(*basket[1:], sep=' ')