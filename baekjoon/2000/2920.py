"""2920.py
음계
https://www.acmicpc.net/problem/2920
"""

num_list = list(map(int,input().split()))

ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

if num_list == ascending:
    print('ascending')
elif num_list == descending:
    print('descending')
else:
    print('mixed')