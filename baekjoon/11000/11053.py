"""11053.py
가장 긴 증가하는 부분 수열
https://www.acmicpc.net/problem/11053
"""


import sys
input = sys.stdin.readline
print = sys.stdout.write


def bin_search(sequence, num):
    start = 0
    end = len(sequence) - 1
    while start < end - 1:
        middle = (start + end) // 2
        if sequence[middle] == num:
            return middle
        elif sequence[middle] < num:
            start = middle
        else:
            end = middle

    if sequence[start] >= num:
        return start
    else:
        return end


N = int(input())
A = list(map(int, input().split()))

sequence = [A[0]]

for i in range(1, N):
    if A[i] > sequence[-1]:
        sequence.append(A[i])
    elif A[i] < sequence[-1]:
        sequence[bin_search(sequence, A[i])] = A[i]
print(f'{len(sequence)}\n')
