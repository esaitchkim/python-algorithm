"""17286.py
유미
https://www.acmicpc.net/problem/17286
"""

"""
세 사람의 좌표는 고정이므로 사람 사이의 거리를 미리 계산해둔다.
각 사람에게 먼저 가는 경우의 최단 거리는 유미가 해당 사람에게 가는 거리 + 해당 사람 외의 두 사람간의 거리 + 해당 사람에서 가장 가까운 사람의 거리
위 거리에 대해서 세 사람 중 가장 짧은 사람 구하면 된다.
"""

yumi = tuple(map(int, input().split()))
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))


yumi_to_a = pow(pow((yumi[0] - a[0]), 2) + pow((yumi[1] - a[1]), 2), 0.5)
yumi_to_b = pow(pow((yumi[0] - b[0]), 2) + pow((yumi[1] - b[1]), 2), 0.5)
yumi_to_c = pow(pow((yumi[0] - c[0]), 2) + pow((yumi[1] - c[1]), 2), 0.5)
a_to_b = pow(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2), 0.5)
a_to_c = pow(pow((a[0] - c[0]), 2) + pow((a[1] - c[1]), 2), 0.5)
b_to_c = pow(pow((b[0] - c[0]), 2) + pow((b[1] - c[1]), 2), 0.5)

print(int(min((yumi_to_a + min(a_to_b, a_to_c)+b_to_c), (yumi_to_b + min(a_to_b, b_to_c) + a_to_c), (yumi_to_c + min(a_to_c, b_to_c) + a_to_b))))
