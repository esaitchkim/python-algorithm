"""10807.py
개수 세기
https://www.acmicpc.net/problem/10807
"""

N = int(input())
num_list = list(map(int,input().split()))
v = int(input())

cnt = 0
for i in num_list:
    if i == v:
        cnt+=1

print(cnt)