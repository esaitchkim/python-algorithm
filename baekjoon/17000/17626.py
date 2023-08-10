"""17626.py
Four Squares
https://www.acmicpc.net/problem/17626
"""

n = int(input())
res = 4

for i in range(int(pow(n, 0.5)), 0, -1):
    num1 = n-(i**2)
    if num1 == 0:
        res = 1
        break

    for j in range(int(pow(num1, 0.5)), 0, -1):
        num2 = num1-(j**2)
        if num2 == 0:
            res = 2
            break
        if pow(num2, 0.5).is_integer():
            res = min(res, 3)
            break
print(res)
