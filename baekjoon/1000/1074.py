"""1074.py
Z
https://www.acmicpc.net/problem/1074
"""

N, r, c = map(int, input().split())
min_r = 0
max_r = 2**N - 1
min_c = 0
max_c = 2**N - 1
cnt = 0

while True:
    r_interval = max_r - min_r
    c_interval = max_c - min_c
    if min_r <= r <= min_r + r_interval//2:
        if min_c <= c <= min_c + c_interval//2:
            max_c = min_c + c_interval//2
        else:
            cnt += (r_interval + 1)//2 * (c_interval + 1)//2
            min_c = max_c - c_interval//2
        max_r = min_r + r_interval//2
    else:
        cnt += (r_interval + 1)//2 * (c_interval + 1)
        if min_c <= c <= min_c + c_interval//2:
            max_c = min_c + c_interval//2
        else:
            cnt += (r_interval + 1)//2 * (c_interval + 1)//2
            min_c = max_c - c_interval//2
        min_r = max_r - r_interval//2
    if min_r == max_r and min_c == max_c:
        break
print(cnt)
