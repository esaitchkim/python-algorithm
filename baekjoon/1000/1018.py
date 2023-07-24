"""1018.py
체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
"""


chess_board = [
    [
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
    ],
    [
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
        ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
    ]
]

N, M = map(int, input().split())
my_board = []
change_cnt = 64

for _ in range(N):
    my_board.append(list(input()))

for i in range(0, N-7):
    for j in range(0, M-7):
        tmp_cnt1 = 0
        tmp_cnt2 = 0
        for x in range(8):
            for y in range(8):
                if chess_board[0][x][y] != my_board[i+x][j+y]:
                    tmp_cnt1 += 1
                if chess_board[1][x][y] != my_board[i+x][j+y]:
                    tmp_cnt2 += 1
        change_cnt = min(change_cnt, tmp_cnt1, tmp_cnt2)

print(change_cnt)
