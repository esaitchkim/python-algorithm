"""20041.py
Escaping
https://www.acmicpc.net/problem/20041
"""

"""
도둑이 잡히지 않으려면 도둑은 계속 한 방향으로만 무한히 뛰어가야한다고 생각했음
도둑의 X 좌표 기준으로 왼쪽의 경찰을 L, 오른쪽의 경찰을 R로 두고
R의 경찰들이 도둑의 Y좌표까지 직선으로 도달하는 거리, 도둑이 X에서 경찰의 X좌표까지 가는 거리를 비교, 도둑이 더 짧은 거리여야지 성공

유사하게 도둑의 Y좌표를 기준으로 위의 경찰을 T, 아래의 경찰을 B로 두고
T의 경찰을이 도둑의 X좌표까지 직선으로 도달하는 거리, 도둑이 Y에서 경찰의 Y좌표까지 가는 거기를 비교, 도둑이 더 짧은 거리여야지 성공
"""


import sys
input = sys.stdin.readline
N = int(input())

police_list = [tuple(map(int, input().split())) for _ in range(N)]
thief = tuple(map(int, input().split()))

t_police = [police for police in police_list if police[1] > thief[1]]
l_police = [police for police in police_list if police[0] < thief[0]]
r_police = [police for police in police_list if police[0] > thief[0]]
b_police = [police for police in police_list if police[1] < thief[1]]

if len(t_police) == 0 or len(l_police) == 0 or len(r_police) == 0 or len(b_police) == 0:
    print('YES')
elif all(y-thief[1] < abs(x - thief[0]) for x, y in t_police) or all(thief[0] - x < abs(y - thief[1]) for x, y in l_police) or all(x - thief[0] < abs(y - thief[1]) for x, y in r_police) or all(thief[1] - y < abs(x - thief[0]) for x, y in b_police):
    print('YES')
else:
    print('NO')
