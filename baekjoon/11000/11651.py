"""11651.py
좌표 정렬하기 2
https://www.acmicpc.net/problem/11651
"""
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

point_dict = {}
for _ in range(N):
    x, y = map(int, input().split())
    if point_dict.get(y) is None:
        point_dict[y] = [x]
    else:
        point_dict[y].append(x)

key_list = sorted(point_dict.keys())

for y in key_list:
    x_list = sorted(point_dict[y])
    for x in x_list:
        print(f'{x} {y}\n')
