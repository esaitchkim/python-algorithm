"""1676.py
팩토리얼 0의 개수
https://www.acmicpc.net/problem/1676
"""


N = int(input())

cnt_2 = 0
cnt_5 = 0

for i in range(N,0,-1):
    num = i
    while num%2==0:
        num//=2
        cnt_2+=1
    while num%5==0:
        num//=5
        cnt_5+=1
    
print(min(cnt_2,cnt_5))