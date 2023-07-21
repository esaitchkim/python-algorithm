"""2588.py
곱셈
https://www.acmicpc.net/problem/2588
"""

num_1 = int(input())
num_2 = input()

for digit in num_2[::-1]:
    print(num_1 * int(digit))

print(num_1*int(num_2))