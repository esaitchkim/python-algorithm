"""2439.py
별 찍기 - 2
https://www.acmicpc.net/problem/2439
"""

N = int(input())
print(*[('*'*i).rjust(N) for i in range(1,N+1)], sep='\n')