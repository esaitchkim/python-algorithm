"""2805.py
나무 자르기
https://www.acmicpc.net/problem/2805
"""

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

res_h = 0
min_h = 0
max_h = max(tree_list)

while min_h <= max_h:
    mid_h = (max_h + min_h)//2
    get_tree = sum([tree - mid_h if tree > mid_h else 0 for tree in tree_list])
    if get_tree >= M:
        if res_h < mid_h:
            res_h = mid_h
        min_h = mid_h + 1
    else:
        max_h = mid_h - 1

print(res_h)

# 다른 풀이를 보니 Counter 등을 이용해서 get_tree 부분의 반복 횟수를 줄이는 방식으로 시간 단축이 가능한 것 같음