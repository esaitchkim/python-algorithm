"""9086.py
문자열
https://www.acmicpc.net/problem/9086
"""

T = int(input())

str_list = []

for _ in range(T):
    str_list.append(input())

for s in str_list:
    print(s[0],s[-1], sep='')