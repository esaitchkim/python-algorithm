"""2164.py
카드2
https://www.acmicpc.net/problem/2164
"""

from collections import deque

N = int(input())

card_list = deque([i for i in range(N,0,-1)])
num = card_list.pop()

while len(card_list)>0:
    card_list.appendleft(card_list.pop())
    num = card_list.pop()

print(num)