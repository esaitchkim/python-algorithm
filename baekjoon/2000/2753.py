"""2753.py
윤년
https://www.acmicpc.net/problem/2753
"""

year_ = int(input())

if (year_%4 == 0 and year_%100 != 0) or year_%400 == 0:
    print(1)
else:
    print(0)