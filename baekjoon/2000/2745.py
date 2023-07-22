"""2745.py
진법 변환
https://www.acmicpc.net/problem/2745
"""

DIFF = 55

N, B = input().split()
B = int(B)

base_10 = 0
for idx, digit in enumerate(N[::-1]):
    if digit.isnumeric():
        base_10+= int(digit)*(B**idx)
    else:
        base_10+= (ord(digit)-DIFF)*(B**idx)

print(base_10)