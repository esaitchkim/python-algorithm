"""2475.py
검증수
https://www.acmicpc.net/problem/2475
"""

num_list = list(map(int,input().split()))
res = sum([i*i for i in num_list])%10

print(res)