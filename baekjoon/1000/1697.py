"""1697.py
숨바꼭질
https://www.acmicpc.net/problem/1697
"""

from collections import deque
N, K = map(int, input().split())
visited = [False] * 200_001
queue = deque()
cnt = 0
queue.append([N])
visited[N] = True

while cnt < abs(K-N):
    x_list = queue.popleft()
    move_list = []
    cnt += 1
    for x in x_list:
        if x > 0 and not visited[x-1]:
            move_list.append(x-1)
            visited[x-1] = True
        if x < K and not visited[x+1]:
            move_list.append(x+1)
            visited[x+1] = True
        if x < K and not visited[x*2]:
            move_list.append(x*2)
            visited[x*2] = True
    if K in move_list:
        break
    queue.append(move_list)
print(cnt)
