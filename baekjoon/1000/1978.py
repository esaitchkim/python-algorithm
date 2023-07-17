"""1978.py
소수 찾기
https://www.acmicpc.net/problem/1978
"""

N = int(input())

num_list = list(map(int, input().split()))
prime_list = [True for _ in range(1001)]
prime_list[0] = False
prime_list[1] = False

for i in range(2, 1001):
    for j in range(2, (1000//i)+1):
        if not prime_list[i]:
            break
        prime_list[i*j] = False

prime_cnt = 0
for n in num_list:
    if prime_list[n]:
        prime_cnt += 1

print(prime_cnt)
