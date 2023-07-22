"""2444.py
별 찍기 - 7
https://www.acmicpc.net/problem/2444
"""

N = int(input())

for i in range(1, N):
    print(' '*(N-i), '*'*(i*2-1), sep='')
print('*'*(N*2-1))
for i in range(N-1, 0, -1):
    print(' '*(N-i), '*'*(i*2-1), sep='')
