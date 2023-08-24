"""18221.py
교수님 저는 취업할래요
https://www.acmicpc.net/problem/18221
"""

import sys
input = sys.stdin.readline

N = int(input())
teacher = [-1, -1]
seongkyu = [1001, 1001]
classroom = []
flag = False
for i in range(N):
    lines = list(map(int, input().split()))
    if 5 in lines:
        teacher = [i, lines.index(5)]
    if 2 in lines:
        seongkyu = [i, lines.index(2)]
    classroom.append(lines)

distance = ((teacher[0] - seongkyu[0])**2) + ((teacher[1] - seongkyu[1])**2)

if distance < 5*5:
    flag = False
else:
    if teacher[0] == seongkyu[0]:
        cnt = 0
        for i in range(min(seongkyu[1], teacher[1]) + 1, max(teacher[1], seongkyu[1])):
            if classroom[teacher[0]][i] == 1:
                cnt += 1
        if cnt >= 3:
            flag = True

    elif teacher[1] == seongkyu[1]:
        cnt = 0
        for i in range(min(seongkyu[0], teacher[0]) + 1, max(teacher[0], seongkyu[0])):
            if classroom[i][teacher[1]] == 1:
                cnt += 1
        if cnt >= 3:
            flag = True

    else:
        cnt = 0
        for i in range(min(seongkyu[0], teacher[0]), max(seongkyu[0], teacher[0]) + 1):
            for j in range(min(seongkyu[1], teacher[1]), max(seongkyu[1], teacher[1]) + 1):
                if classroom[i][j] == 1:
                    cnt += 1
        if cnt >= 3:
            flag = True

print(1 if flag else 0)
