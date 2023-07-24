"""9063.py
대지
https://www.acmicpc.net/problem/9063
"""

N = int(input())

min_x, min_y = 10001, 10001
max_x, max_y = -10001, -10001
for _ in range(N):
    x, y = map(int, input().split())
    min_x = x if x < min_x else min_x
    min_y = y if y < min_y else min_y
    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_y

print(abs(max_x-min_x)*abs(max_y-min_y))
