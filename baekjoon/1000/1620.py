"""1620.py
나는야 포켓몬 마스터 이다솜
https://www.acmicpc.net/problem/1620
"""
import sys

input = sys.stdin.readline
print = sys.stdout.write


N, M = map(int, input().split())

pokemon_num_dict = {}
pokemon_name_dict = {}

for i in range(1, N+1):
    pokemon = input().rstrip()
    pokemon_num_dict[i] = pokemon
    pokemon_name_dict[pokemon] = i

for _ in range(M):
    question = input().rstrip()
    if question.isnumeric():
        print(f'{pokemon_num_dict[int(question)]}\n')
    else:
        print(f'{pokemon_name_dict[question]}\n')
