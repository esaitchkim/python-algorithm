"""9933.py
민균이의 비밀번호
https://www.acmicpc.net/problem/9933
"""

N = int(input())

password_dict = {}

for _ in range(N):
    password = input()
    password_dict[password] = password[::-1]


for key in password_dict.keys():
    real_password = password_dict.get(password_dict[key])
    if real_password is not None:
        password_len = len(real_password)
        middle_word = real_password[password_len//2]
        print(password_len, middle_word, sep=' ')
        break
