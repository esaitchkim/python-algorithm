"""11866.py
요세푸스 문제 0
https://www.acmicpc.net/problem/11866
"""

N, K = map(int, input().split())
num_list = [i for i in range(1,N+1)]
print_list = []
idx = 0
while len(num_list)>0:
    idx+=(K-1)
    idx%=len(num_list)
    print_list.append(num_list.pop(idx))

print('<',end='')
print(*print_list, sep=', ', end='')
print('>')