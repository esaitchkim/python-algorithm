"""1388.py
바닥 장식
https://www.acmicpc.net/problem/1388
"""

N, M = map(int, input().split())

floor = []
cnt = 0
for _ in range(N):
    line = list(input())
    floor.append(line)
    for i in range(len(line)):
        if line[i] == '-':
            if i == 0:
                cnt += 1
            else:
                if line[i-1] == '-':
                    continue
                else:
                    cnt += 1

for j in range(M):
    for i in range(N):
        if floor[i][j] == '|':
            if i == 0:
                cnt += 1
            else:
                if floor[i-1][j] == '|':
                    continue
                else:
                    cnt += 1

print(cnt)
