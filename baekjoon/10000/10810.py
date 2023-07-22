"""10810.py
공 넣기
https://www.acmicpc.net/problem/10810
"""

N, M = map(int, input().split())

basket = [0 for _ in range(N+1)]

for _ in range(M):
    i, j, k = map(int,input().split())
    basket[i:j+1] = [k] *(j - i + 1)
print(*basket[1:], sep=' ')