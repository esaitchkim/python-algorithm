"""10814.py
나이순 정렬
https://www.acmicpc.net/problem/10814
"""
import sys
from collections import defaultdict
input = sys.stdin.readline
write = sys.stdout.write
N = int(input().rstrip())

user_dict = defaultdict(list)
for _ in range(N):
    age, user = map(str, input().rstrip().split())
    age = int(age)
    
    user_dict[age].append(user)

for age in sorted(user_dict.keys()):
    user_list = user_dict[age]
    for user in user_list:
        write(f"{age} {user}\n")