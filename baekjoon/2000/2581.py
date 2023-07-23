"""2581.py
소수
https://www.acmicpc.net/problem/2581
"""

M = int(input())
N = int(input())

prime_list = [i for i in range(N+1)]
prime_list[1] = 0
min_prime = N
for i in range(2, N+1):
    if prime_list[i]:
        if M <= prime_list[i] < min_prime:
            min_prime = prime_list[i]
        for j in range(i+i, N+1, i):
            prime_list[j] = 0

prime_list = prime_list[M:]
sum_prime = sum(prime_list)
if sum_prime:
    print(sum_prime)
    print(min_prime)
else:
    print(-1)
