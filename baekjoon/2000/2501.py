"""2501.py
약수 구하기
https://www.acmicpc.net/problem/2501
"""

N, K = map(int, input().split())

cnt = 0
num = 1

while num <= N:
    if N % num == 0:
        cnt += 1
    if cnt == K:
        break
    num += 1

if cnt != K:
    print(0)
else:
    print(num)
