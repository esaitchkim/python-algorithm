"""19532.py
수학은 비대면강의입니다
https://www.acmicpc.net/problem/19532
"""

a, b, c, d, e, f = map(int, input().split())

flag = False
for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i+b*j == c and d*i+e*j == f:
            print(i, j, sep=' ')
            flag = True
            break
    if flag:
        break
