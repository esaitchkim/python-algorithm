"""11047.py
동전 0
https://www.acmicpc.net/problem/11047
"""

N, K = map(int, input().split())
coin_list = [int(input()) for _ in range(N)]
coin_cnt = 0
for coin in coin_list[::-1]:
    cnt = K//coin
    coin_cnt += cnt
    K -= (cnt * coin)
    if K == 0:
        break

print(coin_cnt)
