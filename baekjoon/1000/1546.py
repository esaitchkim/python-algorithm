"""1546.py
평균
https://www.acmicpc.net/problem/1546
"""

N = int(input())
scores = list(map(int,input().split()))
print((sum(scores)/max(scores))*100/N)