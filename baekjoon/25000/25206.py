"""25206.py
너의 평점은
https://www.acmicpc.net/problem/25206
"""

grade_scale = {'A+': 4.5, 'A0': 4.0,
               'B+': 3.5, 'B0': 3.0,
               'C+': 2.5, 'C0': 2.0,
               'D+': 1.5, 'D0': 1.0,
               'F': 0.0, 'P': None}

total_cc = 0
total_grade = 0

for _ in range(20):
    major, cc, grade = input().split()
    cc = float(cc)
    grade = grade_scale[grade]
    if grade is None:
        continue
    total_cc += cc
    total_grade += (cc*grade)

print(total_grade/total_cc)
