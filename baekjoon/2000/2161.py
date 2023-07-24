"""2161.py
카드1
https://www.acmicpc.net/problem/2161
"""
from collections import deque

N = int(input())

card_list = deque([i for i in range(N, 0, -1)])
print(card_list.pop(), end='')
while len(card_list) > 0:
    card_list.appendleft(card_list.pop())
    print(f' {card_list.pop()}', end='')
