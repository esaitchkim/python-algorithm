"""9372.py
상근이의 여행
https://www.acmicpc.net/problem/9372
"""
import sys
input = sys.stdin.readline
print = sys.stdout.write


def dfs(cntry, visit, node, cnt):
    visit[node] = 1
    for i in cntry[node]:
        if visit[i] == 0:
            cnt = dfs(cntry, visit, i, cnt+1)
    return cnt


T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().rstrip().split())
    cntry = [[] for _ in range(N+1)]
    visit = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        cntry[a].append(b)
        cntry[b].append(a)

    print(str(dfs(cntry, visit, 1, 0))+'\n')
