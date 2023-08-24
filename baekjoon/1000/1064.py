"""1064.py
평행사변형
https://www.acmicpc.net/problem/1064
"""

# 3개의 사각형이 생길 수 있음
# 1. AB, BC를 각 변으로 하는 사각형
# 2. AB, AC를 각 변으로 하는 사각형
# 3. AC, BC를 각 변으로 하는 사각형

xA, yA, xB, yB, xC, yC = map(int, input().split())
m1 = None
m2 = None
# 세 점이 일직선인 경우
if xA != xB:
    m1 = (yA - yB)/(xA - xB)
if xB != xC:
    m2 = (yB - yC)/(xB - xC)
if m1 == m2:
    print(-1)
else:
    parallelogram1 = (pow((xA - xB)**2 + (yA - yB)**2, 0.5) + pow((xB - xC)**2 + (yB - yC)**2, 0.5)) * 2
    parallelogram2 = (pow((xA - xB)**2 + (yA - yB)**2, 0.5) + pow((xA - xC)**2 + (yA - yC)**2, 0.5)) * 2
    parallelogram3 = (pow((xA - xC)**2 + (yA - yC)**2, 0.5) + pow((xB - xC)**2 + (yB - yC)**2, 0.5)) * 2
    print(max(parallelogram1, parallelogram2, parallelogram3) - min(parallelogram1, parallelogram2, parallelogram3))
