"""11022.py
A+B - 8
https://www.acmicpc.net/problem/11022
"""

T = int(input())

for i in range(1,T+1):
    A, B = map(int,input().split())
    print(f'Case #{i}: {A} + {B} = {A+B}')