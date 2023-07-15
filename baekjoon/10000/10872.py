"""10872.py
팩토리얼
https://www.acmicpc.net/problem/10872
"""

N = int(input())
res = 1
for i in range(1,N+1):
    res *= i
print(res)