"""1193.py
분수찾기
https://www.acmicpc.net/problem/1193
"""


X = int(input())

cnt = 0

while True:
    if X-cnt <= 0:
        break
    X -= cnt
    cnt += 1


a, b = 1, cnt
a += (X-1)
b -= (X-1)
if cnt % 2 == 0:
    print(f'{a}/{b}')
else:
    print(f'{b}/{a}')
