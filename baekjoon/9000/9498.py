"""9498.py
시험성적
https://www.acmicpc.net/problem/9498
"""

score = int(input())
print('A' if 90 <= score <=100 else 'B' if 80 <= score <= 89 else 'C' if 70 <= score <=79 else 'D' if 60 <= score <= 69 else 'F')