"""15829.py
Hashing
https://www.acmicpc.net/problem/15829
"""

M = 1234567891
r = 31
L = int(input())
input_str = input()
res = 0

for i in range(L):
    res += (ord(input_str[i])-96)*pow(r,i)

res%=M
print(res)