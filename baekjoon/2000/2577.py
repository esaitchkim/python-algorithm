"""2577.py
숫자의 개수
https://www.acmicpc.net/problem/2577
"""

A = int(input())
B = int(input())
C = int(input())

print(*(str(A*B*C).count(str(i)) for i in range(10)), sep='\n')