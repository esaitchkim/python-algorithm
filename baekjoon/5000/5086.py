"""5086.py
배수와 약수
https://www.acmicpc.net/problem/5086
"""

while True:
    num_1, num_2 = map(int, input().split())
    if num_1 == num_2 == 0:
        break

    if num_1 % num_2 == 0:
        print('multiple')
    elif num_2 % num_1 == 0:
        print('factor')
    else:
        print('neither')
