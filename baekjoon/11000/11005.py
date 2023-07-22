"""11005.py
진법 변환 2
https://www.acmicpc.net/problem/11005
"""

DIFF = 55
N, B = map(int,input().split())

base_B = ''
while N>0:
    mod = N%B
    if mod>=10:
        mod = chr(mod+DIFF)
    else:
        mod = str(mod)
    base_B+=mod
    N//=B

print(base_B[::-1])