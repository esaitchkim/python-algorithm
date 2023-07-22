"""10988.py
팰린드롬인지 확인하기
https://www.acmicpc.net/problem/10988
"""

word = input()
print(1) if word == word[::-1] else print(0)
