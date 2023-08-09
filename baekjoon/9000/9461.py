"""9461.py
파도반 수열
https://www.acmicpc.net/problem/9461
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

padovan_sequence = [1] * 101

for i in range(4, 101):
    padovan_sequence[i] = padovan_sequence[i-2] + padovan_sequence[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(f'{padovan_sequence[N]}\n')
