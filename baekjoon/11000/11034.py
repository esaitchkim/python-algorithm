"""11034.py
캥거루 세마리2
https://www.acmicpc.net/problem/11034
"""

while True:
    try:
        A, B, C = map(int, input().split())
        print(max(B-A-1, C-B-1))
    except:
        break
