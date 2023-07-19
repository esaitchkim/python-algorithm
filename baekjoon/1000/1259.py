"""1259.py
팰린드롬수
https://www.acmicpc.net/problem/1259
"""

while True:
    input_num = input()
    if input_num == '0':
        break
    digits = len(input_num)
    flag = True
    for i in range(round(digits/2)):
        if input_num[i] != input_num[-1-i]:
            flag = False
            break
    
    if flag:
        print('yes')
    else:
        print('no')