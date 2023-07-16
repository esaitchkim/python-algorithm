"""10809.py
알파벳 찾기
https://www.acmicpc.net/problem/10809
"""

S = input()
print(*(S.find(s) for s in 'abcdefghijklmnopqrstuvwxyz'), sep=' ')