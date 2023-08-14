"""11279.py
최대 힙
https://www.acmicpc.net/problem/11279
"""

from heapq import heappop, heappush
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
max_heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(max_heap) == 0:
            print('0\n')
        else:
            print(f'{-heappop(max_heap)}\n')
    else:
        heappush(max_heap, -num)
