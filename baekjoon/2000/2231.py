"""2231.py
분해합
https://www.acmicpc.net/problem/2231
"""

N = int(input())
res = 0
for i in range(N//2, N):
    s = i
    str_i = str(i)
    for digit_i in str_i:
        s += int(digit_i)
    if s == N:
        res = i
        break

print(res)
