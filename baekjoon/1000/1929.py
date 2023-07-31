"""1929.py
소수 구하기
https://www.acmicpc.net/problem/1929
"""

import sys
print = sys.stdout.write

M, N = map(int, input().split())

primes = [True]*(N+1)
primes[0] = False
primes[1] = False

for i in range(2, N+1):
    if primes[i]:
        for j in range(i+i, N+1, i):
            primes[j] = False

for i in range(M, len(primes)):
    if primes[i]:
        print(f'{i}\n')
