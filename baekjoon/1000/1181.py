"""1181.py
단어 정렬
https://www.acmicpc.net/problem/1181
"""

word_dict = {}
N = int(input())

for _ in range(N):
    word = input()
    len_word = len(word)
    if word_dict.get(len_word) is None:
        word_dict[len_word] = set()
    
    word_dict[len_word].add(word)

key_list = sorted(list(word_dict.keys()))

for len_word in key_list:
    print(*sorted(list(word_dict[len_word])), sep='\n')