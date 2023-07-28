"""10773.py
제로
https://www.acmicpc.net/problem/10773
"""

import sys

input = sys.stdin.readline

K = int(input())
num_list = [0]*K
idx = 0
res = 0
for _ in range(K):
    num = int(input())
    if num==0:
        idx-=1
        erase_num = num_list[idx]
        num_list[idx] = 0
        res -= erase_num
    else:
        res += num
        num_list[idx] = num
        idx +=1

print(res)