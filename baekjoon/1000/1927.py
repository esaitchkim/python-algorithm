"""1927.py
최소 힙
https://www.acmicpc.net/problem/1927
"""

from heapq import heappop, heappush
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
min_heap = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(min_heap) == 0:
            print('0\n')
        else:
            print(f'{heappop(min_heap)}\n')
    else:
        heappush(min_heap, num)
