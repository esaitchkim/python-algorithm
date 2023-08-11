"""1541.py
잃어버린 괄호
https://www.acmicpc.net/problem/1541
"""

exp_list = input().split('-')
res = sum([int(i) for i in exp_list[0].split('+')]) - sum([int(num) for i in range(1, len(exp_list)) for num in exp_list[i].split('+')])
print(res)
