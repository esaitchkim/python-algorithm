"""2884.py
알람 시계
https://www.acmicpc.net/problem/2884
"""

H, M = map(int, input().split())

if M<45:
    res_m = M+15
    res_h = H - 1 if H>0 else 23
else:
    res_m = M-45
    res_h = H

print(res_h, res_m, sep=' ')