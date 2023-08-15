"""11286.py
절댓값 힙
https://www.acmicpc.net/problem/11286
"""

import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
print = sys.stdout.write

heap = []
key_dict = defaultdict(int)

N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(heap) > 0:
            element = heappop(heap)
            if key_dict[-element] > 0:
                key_dict[-element] -= 1
                element = -element
            else:
                key_dict[element] -= 1
            print(f'{element}\n')
        else:
            print(f'0\n')
    else:
        key_dict[num] += 1
        heappush(heap, abs(num))
