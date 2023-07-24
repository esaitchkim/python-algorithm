"""2748.py
피보나치 수 2
https://www.acmicpc.net/problem/2748
"""

n = int(input())

fibonacci = [0]*(n+1)
fibonacci[1] = 1
for i in range(2, n+1):
    fibonacci[i] = fibonacci[i-2] + fibonacci[i-1]

print(fibonacci[n])
