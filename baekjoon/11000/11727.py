"""11727.py
2×n 타일링 2
https://www.acmicpc.net/problem/11727
"""

square_list = [1] * 1001
for i in range(2, len(square_list)):
    square_list[i] = square_list[i-2]*2 + square_list[i-1]

n = int(input())
print(square_list[n] % 10007)
