"""11021.py
A+B -7
https://www.acmicpc.net/problem/11021
"""

T = int(input())

for i in range(1,T+1):
    A,B = map(int,input().split())
    print(f'Case #{i}: {A+B}')