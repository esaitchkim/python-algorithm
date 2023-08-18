"""5525.py
IOIOI
https://www.acmicpc.net/problem/5525
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

cnt = 0
i = S.find('I')
j = i

while i < M:
    if S[i:i+3] == 'IOI':
        i += 2
        if i - j == 2 * N:
            cnt += 1
            j += 2
    else:
        i += 1
        j = i

print(cnt)
