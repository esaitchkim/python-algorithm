"""10162.py
전자레인지
https://www.acmicpc.net/problem/10162
"""

T = int(input())

A = 300
B = 60
C = 10

btn_cnt_list = [0, 0, 0]

btn_cnt_list[0] = (T//A)
T -= (A*btn_cnt_list[0])

btn_cnt_list[1] = (T//B)
T -= (B*btn_cnt_list[1])

btn_cnt_list[2] = (T//C)
T -= (C*btn_cnt_list[2])

if T == 0:
    print(*btn_cnt_list, sep=' ')
else:
    print(-1)
