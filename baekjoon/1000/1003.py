"""1003.py
피보나치 함수
https://www.acmicpc.net/problem/1003
"""

cnt_0_list = [0] * 41
cnt_0_list[0] = 1
cnt_1_list = [0] * 41
cnt_1_list[1] = 1
for i in range(2, 41):
    cnt_0_list[i] = cnt_0_list[i-1] + cnt_0_list[i-2]
    cnt_1_list[i] = cnt_1_list[i-1] + cnt_1_list[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(cnt_0_list[N], cnt_1_list[N], sep=' ')
