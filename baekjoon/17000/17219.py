"""17219.py
비밀번호 찾기
https://www.acmicpc.net/problem/17219
"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())

password_dict = {}

for _ in range(N):
    site, pw = input().rstrip().split()
    password_dict[site] = pw

for _ in range(M):
    print(f'{password_dict[input().rstrip()]}\n')
