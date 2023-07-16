"""4153.py
직각삼각형
https://www.acmicpc.net/problem/4153
"""

while True:
    a, b, c = map(int, input().split())
    if a==b==c==0:
        break
    a*=a
    b*=b
    c*=c

    max_num = max(a,b,c)
    if max_num*2 == a+b+c:
        print('right')
    else:
        print('wrong')