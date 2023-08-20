"""4197.py
Logo
https://www.acmicpc.net/problem/4197
"""

import sys
from math import cos, sin, radians

input = sys.stdin.readline
print = sys.stdout.write

test_cnt = int(input())

for t in range(test_cnt):
    command_cnt = int(input())
    n_degree = 0
    x, y = 0, 0
    for _ in range(command_cnt):
        command, num = input().rstrip().split()
        num = int(num)

        if command == 'fd':
            x += cos(radians(n_degree)) * num
            y += sin(radians(n_degree)) * num
        elif command == 'bk':
            x -= cos(radians(n_degree)) * num
            y -= sin(radians(n_degree)) * num
        elif command == 'lt':
            n_degree = (n_degree+num) % 360
        elif command == 'rt':
            n_degree = (n_degree-num) % 360
    print(f'{round(pow((x**2 + y**2), 0.5))}\n')
