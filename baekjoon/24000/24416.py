"""24416.py
알고리즘 수업 - 피보나치 수 1
https://www.acmicpc.net/problem/24416
"""

n = int(input())

code_1 = [0, 1, 1, 2, 3] + [0]*36
code_2 = [0, 0, 0, 1, 2] + [0]*36

for i in range(5, 41):
    code_1[i] = code_1[i-2] + code_1[i-1]
    code_2[i] = code_2[i-1] + 1

print(code_1[n], code_2[n], sep=' ')
