"""2720.py
세탁소 사장 동혁
https://www.acmicpc.net/problem/2720
"""

T = int(input())
for _ in range(T):
    C = int(input())
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    quarter = C//25
    C-=(25*quarter)
    dime = C//10
    C-=(10*dime)
    nickel = C//5
    C-=(5*nickel)
    penny = C//1
    print(f'{quarter} {dime} {nickel} {penny}')