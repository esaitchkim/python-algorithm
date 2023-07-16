"""3052.py
나머지
https://www.acmicpc.net/problem/3052
"""

mod_set = set()
add = mod_set.add
for _ in range(10):
    add(int(input())%42)
print(len(mod_set))