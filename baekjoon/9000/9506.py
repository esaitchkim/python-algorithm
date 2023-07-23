"""9506.py
약수들의 합
https://www.acmicpc.net/problem/9506
"""

while True:
    n = int(input())
    if n == -1:
        break

    left_list = [1]
    right_list = []

    max_num = n//2
    now_num = 2

    while now_num < max_num:
        if n % now_num == 0:
            if n == now_num**2:
                left_list.append(now_num)
                break
            else:
                left_list.append(now_num)
                right_list.append(n//now_num)
                max_num = n//now_num
        now_num += 1

    if sum(left_list) + sum(right_list) == n:
        merge_list = left_list + right_list[::-1]
        print(f'{n} = {" + ".join(map(str,merge_list))}')
    else:
        print(f'{n} is NOT perfect.')
