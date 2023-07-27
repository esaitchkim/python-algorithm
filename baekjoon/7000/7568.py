"""7568.py
덩치
https://www.acmicpc.net/problem/7568
"""

N = int(input())

people_list = []

for _ in range(N):
    x, y = map(int, input().split())
    people_list.append([x, y])


order_list = [N] * N

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if people_list[i][0] < people_list[j][0] and people_list[i][1] < people_list[j][1]:
            continue
        else:
            order_list[i] -= 1

print(*order_list, sep=' ')
