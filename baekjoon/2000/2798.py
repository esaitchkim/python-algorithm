"""2798.py
블랙잭
https://www.acmicpc.net/problem/2798
"""

N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()
res = 0
flag = False
for num_1 in range(0, len(num_list)-2):
    if flag:
        break
    for num_2 in range(num_1+1, len(num_list)-1):
        if flag:
            break
        for num_3 in range(num_2+1, len(num_list)):
            s = num_list[num_1] + num_list[num_2] + num_list[num_3]
            if s == M:
                res = s
                flag = True
                break
            elif s > res:
                if s < M:
                    res = s
                else:
                    break

print(res)
