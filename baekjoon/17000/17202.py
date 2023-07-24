"""17202.py
핸드폰 번호 궁합
https://www.acmicpc.net/problem/17202
"""

A = [int(digit) for digit in input()]
B = [int(digit) for digit in input()]

num_list = [digit for phone_addr in zip(A, B) for digit in phone_addr]

while len(num_list) > 2:
    tmp_list = []
    for i in range(len(num_list)-1):
        tmp_list.append((num_list[i]+num_list[i+1]) % 10)
    num_list = tmp_list

print(*num_list, sep='')
