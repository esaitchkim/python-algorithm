"""2864.py
5와 6의 차이
https://www.acmicpc.net/problem/2864
"""

A, B = input().split()

max_A, max_B = int(A.replace('5', '6')), int(B.replace('5', '6'))
min_A, min_B = int(A.replace('6', '5')), int(B.replace('6', '5'))

print(min_A+min_B, max_A+max_B, sep=' ')
