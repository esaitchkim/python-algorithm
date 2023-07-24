"""1085.py
직사각형에서 탈출
https://www.acmicpc.net/problem/1085
"""

x, y, w, h = map(int, input().split())

min_w = x if x < w - x else w-x
min_h = y if y < h - y else h-y
print(min_w if min_w < min_h else min_h)
