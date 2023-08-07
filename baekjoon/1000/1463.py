"""1463.py
1로 만들기
https://www.acmicpc.net/problem/1463
"""

N = int(input())

res_list = [N] * (N+1)
res_list[0] = -1

for i in range(1, N+1):
    if i % 2 == 0:
        res_list[i] = min(res_list[i//2]+1, res_list[i])
    if i % 3 == 0:
        res_list[i] = min(res_list[i//3]+1, res_list[i])
    res_list[i] = min(res_list[i], res_list[i-1] + 1)

print(res_list[N])
