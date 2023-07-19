"""2609.py
최대공약수와 최소공배수
https://www.acmicpc.net/problem/2609
"""

num1, num2 = map(int,input().split())
(gcd, tmp) = (num1, num2) if num1 > num2 else (num2, num1)

while True:
    gcd, tmp = tmp, gcd%tmp
    if tmp==0:
        break

lcm = (num1//gcd)*num2
print(gcd, lcm)