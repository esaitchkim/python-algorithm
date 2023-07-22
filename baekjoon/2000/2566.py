"""2566.py
최댓값
https://www.acmicpc.net/problem/2566
"""

max_value = -1
max_point = [0, 0]

for i in range(9):
    lines = list(map(int, input().split()))
    tmp_max_value = -1
    tmp_max_idx = 10
    for j in range(9):
        if lines[j] > tmp_max_value:
            tmp_max_value = lines[j]
            tmp_max_idx = j
    if tmp_max_value > max_value:
        max_value = tmp_max_value
        max_point = [i+1, tmp_max_idx+1]

print(max_value)
print(*max_point, sep=' ')
