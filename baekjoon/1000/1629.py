"""1629.py
곱셈
https://www.acmicpc.net/problem/1629
"""

A, B, C = map(int, input().split())
mul_list = [0]*33
mul_list[1] = A % C

bin_B = format(B, 'b').zfill(32) + '0'
mul_flag = [int(i) for i in reversed(bin_B)]

for i in range(2, len(mul_list)):
    mul_list[i] = (mul_list[i-1] * mul_list[i-1]) % C

res = 1

for i in range(len(mul_flag)):
    if mul_flag[i] == 1:
        res = (res * mul_list[i]) % C

print(res)
