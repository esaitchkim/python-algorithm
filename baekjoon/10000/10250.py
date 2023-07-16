"""10250.py
ACM 호텔
https://www.acmicpc.net/problem/10250
"""

from math import ceil

T = int(input())

for _ in range(T):
    H, W, N = map(int,input().split())

    w = str(ceil(N/H)).zfill(2)
    h = N%H
    h = H if h==0 else h
    
    print(h, w, sep='')
