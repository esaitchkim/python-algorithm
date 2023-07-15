"""2675.py
문자열 반복
https://www.acmicpc.net/problem/2675
"""

T = int(input())

for _ in range(T):
    num, S = map(str, input().split(' '))
    S = ''.join([s*int(num) for s in list(S)])
    print(S)