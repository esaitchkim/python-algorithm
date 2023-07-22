"""2563.py
색종이
https://www.acmicpc.net/problem/2563
"""

paper = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
black_area = 0
for _ in range(n):
    w, h = map(int, input().split())

    for i in range(w, w+10):
        paper[i][h:h+10] = [1]*10

for line in paper:
    black_area += sum(line)

print(black_area)
