"""2667.py
단지번호붙이기
https://www.acmicpc.net/problem/2667
"""

import sys
from collections import deque, defaultdict
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
apart = []
apart_cnt = defaultdict(int)
for _ in range(N):
    line = list(input().rstrip())
    apart.append(line)

cnt = 0
for i in range(N):
    for j in range(N):
        if apart[i][j] != "1":
            continue
        queue = deque()
        queue.append((i, j))
        apart[i][j] = '0'
        while len(queue) > 0:
            node_x, node_y = queue.popleft()
            apart_cnt[cnt] += 1
            if 0 < node_x:
                if apart[node_x-1][node_y] == "1":
                    apart[node_x-1][node_y] = "0"
                    queue.append((node_x-1, node_y))
            if node_x < N-1:
                if apart[node_x+1][node_y] == "1":
                    apart[node_x+1][node_y] = "0"
                    queue.append((node_x+1, node_y))
            if 0 < node_y:
                if apart[node_x][node_y-1] == "1":
                    apart[node_x][node_y-1] = "0"
                    queue.append((node_x, node_y-1))
            if node_y < N - 1:
                if apart[node_x][node_y+1] == "1":
                    apart[node_x][node_y+1] = "0"
                    queue.append((node_x, node_y+1))
        cnt += 1

print(f'{len(apart_cnt)}\n')
for i in sorted(apart_cnt.values()):
    print(f'{i}\n')
