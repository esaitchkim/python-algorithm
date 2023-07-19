"""10989.py
수 정렬하기 3
https://www.acmicpc.net/problem/10989
"""

import sys

input = sys.stdin.readline
write = sys.stdout.write

int_list = [0 for _ in range(10001)]
N = int(input().rstrip())
for _ in range(N):
    num = int(input().rstrip())
    int_list[num]+=1

for i in range(10001):
        for _ in range(int_list[i]):
              s = str(i)
              write(s+'\n')