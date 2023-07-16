"""8958.py
OX퀴즈
https://www.acmicpc.net/problem/8958
"""

t = int(input())

for _ in range(t):
    ox_str = input()
    score_list = [0 for _ in range(len(ox_str))]
    if ox_str[0]=='O':
        score_list[0] = 1
    
    for i in range(1,len(score_list)):
        score_list[i] = score_list[i-1] + 1 if ox_str[i]=='O' else 0
    print(sum(score_list))