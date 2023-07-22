"""10798.py
세로읽기
https://www.acmicpc.net/problem/10798
"""

vertical_list = [[] for _ in range(15)]
print_word = ''
for _ in range(5):
    word = input()
    for i in range(len(word)):
        vertical_list[i].append(word[i])


for vertical_str in vertical_list:
    line_str = ''.join(vertical_str)
    print_word += line_str

print(print_word)
