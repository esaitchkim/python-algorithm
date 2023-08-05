"""11399.py
ATM
https://www.acmicpc.net/problem/11399
"""

N = int(input())
p_list = list(map(int, input().split()))

p_list = sorted(p_list)
total_time = sum((p_list[i]*(N-i) for i in range(N)))
print(total_time)
