"""2941.py
크로아티아 알파벳
https://www.acmicpc.net/problem/2941
"""

c_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
c_cnt = 0
for s in c_alphabet:
    c_cnt += word.count(s)
    word = word.replace(s, ' ')

word = word.replace(' ', '')
print(c_cnt+len(word))
