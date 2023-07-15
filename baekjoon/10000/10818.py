"""10818.py
최소, 최대
https://www.acmicpc.net/problem/10818
"""

N = int(input())

num_list = list(map(int, input().split()))

print(min(num_list), max(num_list), sep=' ')