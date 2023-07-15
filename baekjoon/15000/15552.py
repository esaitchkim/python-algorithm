"""15552.py
빠른 A+B
https://www.acmicpc.net/problem/15552
"""

import sys

s_in = sys.stdin.readline
s_out = sys.stdout.write

T = int(s_in())

for i in range(T):
    A, B = map(int, s_in().split())
    s_out(f'{A+B}\n')