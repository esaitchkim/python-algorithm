"""11371.py
The Big Eye in the Sky
https://www.acmicpc.net/problem/11371
"""

import sys
from math import atan2, pi
input = sys.stdin.readline
print = sys.stdout.write

x, y = map(int, input().split())
while (x, y) != (0, 0):
    theta = round((atan2(y, x) / pi) * 180)
    print(f'{theta}\n')
    x, y = map(int, input().split())
