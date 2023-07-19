"""11050.py
이항 계수 1
https://www.acmicpc.net/problem/11050
"""

def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return num
    else:
        return num*factorial(num-1)


N, K = map(int,input().split())

res = factorial(N) // (factorial(K) * factorial(N-K))
print(res)