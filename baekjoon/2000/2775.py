"""2775.py
부녀회장이 될테야
https://www.acmicpc.net/problem/2775
"""

T= int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apart = {}
    apart[0] = [i for i in range(15)]

    for i in range(1,15):
        apart[i] = apart[i-1].copy()
        for j in range(1, 15):
            apart[i][j] += apart[i][j-1]

    print(apart[k][n])