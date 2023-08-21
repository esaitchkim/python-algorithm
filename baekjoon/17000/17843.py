"""17843.py
시계
https://www.acmicpc.net/problem/17843
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())

for _ in range(T):
    h, m, s = map(int, input().split())
    s_d = 360 * (s/60)
    m_d = 360 * ((m * 60 + s)/(60*60))
    h_d = 360 * ((h * 60 * 60 + m * 60 + s)/(12 * 60 * 60))
    aob = abs(h_d - m_d)
    aoc = abs(h_d - s_d)
    boc = abs(m_d - s_d)
    aob = aob if 360 > 2 * aob else 360-aob
    aoc = aoc if 360 > 2 * aoc else 360-aoc
    boc = boc if 360 > 2 * boc else 360-boc

    print(f'{min(aob, aoc, boc)}\n')
