"""11653.py
소인수분해
https://www.acmicpc.net/problem/11653
"""

N = int(input())
num = 2
while N >= num:
    if N % num == 0:
        print(num)
        N //= num
    else:
        num += 1
