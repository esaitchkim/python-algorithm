"""14215.py
세 막대
https://www.acmicpc.net/problem/14215
"""

a, b, c = map(int, input().split())

max_length = max(a, b, c)
three_length = sum([a, b, c])
two_length = three_length - max_length
max_length = max_length if two_length > max_length else two_length - 1

print(two_length + max_length)
