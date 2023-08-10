"""11726.py
2×n 타일링
https://www.acmicpc.net/problem/11726
"""

square_list = [0] * 1001
square_list[1:3] = [1, 2]
for i in range(3, 1001):
    square_list[i] = square_list[i-1] + square_list[i-2]

n = int(input())
print(square_list[n] % 10007)
