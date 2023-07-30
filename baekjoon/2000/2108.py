"""2108.py
통계학
https://www.acmicpc.net/problem/2108
"""

from collections import defaultdict
import sys
input = sys.stdin.readline


N = int(input())

num_dict = defaultdict(int)

for _ in range(N):
    num_dict[int(input())] += 1

num_list = sorted(num_dict.keys())

sum_nums = 0
median_cnt = (N//2)+1
median = None
cnt = 0
mode_list = []
mode_cnt = 0
diff = num_list[-1] - num_list[0]


for num in num_list:
    sum_nums += (num * num_dict[num])
    if cnt < median_cnt:
        cnt += num_dict[num]
        if cnt >= median_cnt:
            median = num

    if num_dict[num] > mode_cnt:
        mode_list = [num]
        mode_cnt = num_dict[num]
    elif num_dict[num] == mode_cnt:
        mode_list.append(num)

print(round(sum_nums/N))
print(median)
print(mode_list[0] if len(mode_list) == 1 else mode_list[1])
print(diff)
