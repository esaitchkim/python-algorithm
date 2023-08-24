"""16937.py
두 스티커
https://www.acmicpc.net/problem/16937
"""

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = []
max_area = 0
for _ in range(N):
    R, C = map(int, input().split())
    stickers.append((R, C))

for i in range(N-1):
    for j in range(i+1, N):
        R1, C1 = stickers[i]
        R2, C2 = stickers[j]
        if R1 + R2 <= H:
            if max(C1, C2) <= W:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if R1 + R2 <= W:
            if max(C1, C2) <= H:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if C1 + C2 <= H:
            if max(R1, R2) <= W:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if C1 + C2 <= W:
            if max(R1, R2) <= H:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if R1 + C2 <= H:
            if max(R2, C1) <= W:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if R1 + C2 <= W:
            if max(R2, C1) <= H:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if R2 + C1 <= H:
            if max(R1, C2) <= W:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area
        if R2 + C1 <= W:
            if max(R1, C2) <= H:
                area = R1*C1 + R2*C2
                max_area = area if max_area < area else max_area

print(max_area)
