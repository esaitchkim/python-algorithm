"""5597.py
과제 안 내신 분..?
https://www.acmicpc.net/problem/5597
"""

students = [False for _ in range(31)]
students[0] = True
for _ in range(28):
    n = int(input())
    students[n] = True

for idx, s in enumerate(students):
    if s == False:
        print(idx)