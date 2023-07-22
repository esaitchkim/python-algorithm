"""1316.py
그룹 단어 체커
https://www.acmicpc.net/problem/1316
"""

N = int(input())
group_word_cnt = 0
for _ in range(N):
    group_list = []
    word = input()
    group_list.append(word[0])
    idx = 1
    while idx < len(word):
        if word[idx] == word[idx-1]:
            idx += 1
            continue
        if word[idx] in group_list:
            group_word_cnt -= 1
            break
        else:
            group_list.append(word[idx])
            idx += 1

    group_word_cnt += 1

print(group_word_cnt)
