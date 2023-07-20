"""2751.py
수 정렬하기 2
https://www.acmicpc.net/problem/2751
"""
import sys

input = sys.stdin.readline
write = sys.stdout.write
N = int(input().strip())

num_dict = {i:True for i in (int(input().strip()) for _ in range(N))}

for i in sorted(num_dict.keys()):
    write(str(i)+'\n')