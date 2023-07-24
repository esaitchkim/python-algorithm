"""1920.py
수 찾기
https://www.acmicpc.net/problem/1920
"""

N = int(input())
A = {key:True for key in map(int, input().split())}
M = int(input())
num_list = list(map(int, input().split()))

print(*[1 if A.get(num) is not None else 0 for num in num_list], sep='\n')
