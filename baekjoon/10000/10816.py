"""10816.py
숫자 카드 2
https://www.acmicpc.net/problem/10816
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
card_list = list(map(int, input().rstrip().split()))
card_dict = {}
for num in card_list:
    if card_dict.get(num) is None:
        card_dict[num] = 1
    else:
        card_dict[num] += 1
M = int(input().rstrip())

print(' '.join('0' if card_dict.get(num) is None
               else str(card_dict[num]) for num in map(int, input().rstrip().split())))
