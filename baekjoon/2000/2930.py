"""2930.py
가위 바위 보
https://www.acmicpc.net/problem/2930
"""

SPR = {'S': {'S': 1, 'P': 2, 'R': 0},
       'P': {'S': 0, 'P': 1, 'R': 2},
       'R': {'S': 2, 'P': 0, 'R': 1}}


R = int(input())
s = input()

N = int(input())

score = 0
max_score = 0

round_dict = {i: {'S': 0, 'P': 0, 'R': 0} for i in range(R)}

for _ in range(N):
    friend_spr = input()
    for round in range(R):
        round_dict[round][friend_spr[round]] += 1

for round in range(R):
    s_score = 0
    p_score = 0
    r_score = 0

    for spr, num in round_dict[round].items():
        score += (SPR[s[round]][spr] * num)
        s_score += (SPR['S'][spr] * num)
        p_score += (SPR['P'][spr] * num)
        r_score += (SPR['R'][spr] * num)
    max_score += max(s_score, p_score, r_score)

print(score)
print(max_score)
