"""2562.py
최댓값
https://www.acmicpc.net/problem/2562
"""

max_int = max_idx = 0

for i in range(1,10):
    input_num = int(input())
    if max_int < input_num:
        max_int = input_num
        max_idx = i

print(max_int, max_idx, sep='\n')