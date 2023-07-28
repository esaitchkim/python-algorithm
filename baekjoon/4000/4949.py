"""4949.py
균형잡힌 세상
https://www.acmicpc.net/problem/4949
"""

import sys

input = sys.stdin.readline
print = sys.stdout.write

input_string = input().rstrip()

while input_string != ".":
    brackets = ''.join([s for s in input_string if s in ('(', ')', '[', ']')])
    while True:
        before_lens = len(brackets)
        brackets = brackets.replace('()', '').replace('[]', '')
        after_lens = len(brackets)
        if before_lens == after_lens:
            break
    if len(brackets) == 0:
        print('yes\n')
    else:
        print('no\n')

    input_string = input().rstrip()
