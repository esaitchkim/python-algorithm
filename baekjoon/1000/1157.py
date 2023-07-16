"""1157.py
단어 공부
https://www.acmicpc.net/problem/1157
"""

word = input().upper()
word_dict = {}
max_cnt = 0
max_alphabet = '?'

for s in word:
    if word_dict.get(s) is not None:
        word_dict[s] += 1
    else:
        word_dict[s] = 1
    
    if word_dict[s] > max_cnt:
        max_cnt = word_dict[s]
        max_alphabet = s
    elif word_dict[s] == max_cnt:
        max_alphabet = '?'

print(max_alphabet)