"""10811.py
바구니 뒤집기
https://www.acmicpc.net/problem/10811
"""

N, M = map(int, input().split())

basket = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int,input().split())
    basket[i:j+1] = basket[j:i-1:-1]
print(*basket[1:], sep=' ')