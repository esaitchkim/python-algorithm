"""2839.py
설탕 배달
https://www.acmicpc.net/problem/2839
"""

N = int(input())
res = -1
for i in range(N//5, -1, -1):
    remain = N-(i*5)
    if remain % 3 == 0:
        res = i+(remain//3)
        break

print(res)
