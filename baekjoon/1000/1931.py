"""1931.py
회의실 배정
https://www.acmicpc.net/problem/1931
"""

import sys
input = sys.stdin.readline

N = int(input())
meeting_list = [list(map(int, input().split())) for _ in range(N)]
meeting_list.sort(key=lambda x: (x[1], x[0]))


def meetingroom_assign(meeting_list, idx, cnt):
    cnt += 1
    res_cnt = cnt
    end_time = meeting_list[idx][1]
    for i in range(idx+1, len(meeting_list)):
        if meeting_list[i][0] >= end_time:
            res_cnt = max(res_cnt, meetingroom_assign(meeting_list, i, cnt))
    return res_cnt


last_time = 0
res_cnt = 0
for start_time, end_time in meeting_list:
    if last_time <= start_time:
        res_cnt +=1
        last_time = end_time

print(res_cnt)
