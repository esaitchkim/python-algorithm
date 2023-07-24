"""5073.py
삼각형과 세 변
https://www.acmicpc.net/problem/5073
"""

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    max_lengths = max(a, b, c)
    lengths_sum = sum([a, b, c])

    # 삼각형 만족 여부
    if a + b + c > max_lengths*2:
        if a == b == c:
            print('Equilateral')
        elif a == b or a == c or b == c:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')
