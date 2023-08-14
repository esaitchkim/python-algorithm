"""21736.py
헌내기는 친구가 필요해
https://www.acmicpc.net/problem/21736
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

campus = []
visited = []
root = None
cnt = 0
for i in range(N):
    lines = list(input().rstrip())
    campus.append(lines)
    visited.append([False if element in ['P', 'O'] else True for element in lines])
    if 'I' in lines:
        root = [i, lines.index('I')]

stack = deque()
stack.append(root)
while len(stack):
    i, j = stack.popleft()

    if i < N-1 and not visited[i+1][j]:
        visited[i+1][j] = True
        if campus[i+1][j] == 'P':
            cnt += 1
        stack.append([i+1, j])

    if j < M-1 and not visited[i][j+1]:
        visited[i][j+1] = True
        if campus[i][j+1] == 'P':
            cnt += 1
        stack.append([i, j+1])

    if 0 < i and not visited[i-1][j]:
        visited[i-1][j] = True
        if campus[i-1][j] == 'P':
            cnt += 1
        stack.append([i-1, j])

    if 0 < j and not visited[i][j-1]:
        visited[i][j-1] = True
        if campus[i][j-1] == 'P':
            cnt += 1
        stack.append([i, j-1])

if cnt:
    print(cnt)
else:
    print('TT')
