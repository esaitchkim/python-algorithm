"""10101.py
삼각형 외우기
https://www.acmicpc.net/problem/10101
"""

angles_sum = 0
angles_set = set()

angle = int(input())
angles_sum += angle
angles_set.add(angle)

angle = int(input())
angles_sum += angle
angles_set.add(angle)

angle = int(input())
angles_sum += angle
angles_set.add(angle)

if angles_sum == 180:
    if len(angles_set) == 1:
        print('Equilateral')
    elif len(angles_set) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
