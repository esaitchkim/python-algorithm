"""3578.py
Holes
https://www.acmicpc.net/problem/3578
"""

h = int(input())

if h == 0:
    print('1')
elif h == 1:
    print('0')
else:
    e_cnt = h//2
    h -= (2*e_cnt)
    if h == 0:
        res = '8'*e_cnt
    else:
        res = '4'+'8'*e_cnt
    print(res)
