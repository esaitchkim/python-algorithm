"""11781.py
그대로 출력하기
https://www.acmicpc.net/problem/11718
"""

buff = []

for _ in range(100):
    try:
        buff.append(input())
    except:
        break

print(*buff, sep='\n')