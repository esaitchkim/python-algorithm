"""2292.py
벌집
https://www.acmicpc.net/problem/2292
"""

N = int(input())
N-=1
cnt = 1

while N>0:
    N-=(6*cnt)
    cnt+=1

print(cnt)