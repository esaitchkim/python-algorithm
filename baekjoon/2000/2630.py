"""2630.py
색종이 만들기
https://www.acmicpc.net/problem/2630
"""


def paper_slice(paper):
    n = len(paper)
    color_cnt = 0
    white = 0
    blue = 0
    for paper_line in paper:
        color_cnt += sum(paper_line)
    if color_cnt == 0:
        return 1, 0
    elif color_cnt == n*n:
        return 0, 1
    else:
        paper_list = [[], [], [], []]
        for i in range(n//2):
            paper_list[0].append(paper[i][:n//2])
            paper_list[1].append(paper[i][n//2:])
        for i in range(n//2, n):
            paper_list[2].append(paper[i][:n//2])
            paper_list[3].append(paper[i][n//2:])

        for i in range(4):
            tmp_white, tmp_blue = paper_slice(paper_list[i])
            white += tmp_white
            blue += tmp_blue
    return white, blue


N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

white, blue = paper_slice(paper)

print(white)
print(blue)
