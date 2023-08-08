"""9095.py
1, 2, 3 더하기

https://www.acmicpc.net/problem/9375
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

factorial = [i for i in range(12)]
factorial[0] = 1
for i in range(1, 12):
    factorial[i] *= factorial[i-1]

res_cnt = [0] * 12

for i in range(1, 12):
    cnt = 0
    n_3 = i//3
    for n3 in range(i//3, -1, -1):
        for n2 in range((i-(n3*3))//2, -1, -1):
            n1 = i - (n3*3) - (n2*2)
            cnt += (factorial[n1 + n2 + n3]//factorial[n3]//factorial[n2]//factorial[n1])
    res_cnt[i] = cnt

T = int(input())
for _ in range(T):
    print(f'{res_cnt[int(input())]}\n')
