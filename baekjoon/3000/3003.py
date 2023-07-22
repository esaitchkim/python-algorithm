"""3003.py
킹, 퀸, 룩, 비숍, 나이트, 폰
https://www.acmicpc.net/problem/3003
"""

having_pieces = list(map(int,input().split()))
set_pieces = [1, 1, 2, 2, 2, 8]

need_pieces = [s_p-h_p for h_p, s_p in zip(having_pieces, set_pieces)]
print(*need_pieces, sep=' ')
