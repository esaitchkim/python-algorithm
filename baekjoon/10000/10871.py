"""10871.py
X보다 작은 수
https://www.acmicpc.net/problem/10871
"""

N, X = map(int,input().split())
N = [i for i in list(map(int,input().split())) if i <X]
print(*N, sep=' ')