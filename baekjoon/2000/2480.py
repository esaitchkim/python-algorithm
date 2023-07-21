"""2480.py
주사위 세개
https://www.acmicpc.net/problem/2480
"""
from collections import Counter

dice_dict = dict(Counter(list(map(int,input().split()))))
reward = 0
pip_list = list(dice_dict.keys())
if len(pip_list) == 1:
    reward = 10_000 + (pip_list[0])*1_000

elif len(pip_list) == 2:
    twice_pip = pip_list[0] if dice_dict[pip_list[0]]==2 else pip_list[1]
    reward = 1_000 + (twice_pip)*100

else:
    max_pip = max(pip_list)
    reward = max_pip * 100

print(reward)