"""28113.py
정보섬의 대중교통
https://www.acmicpc.net/problem/28113
"""

N, A, B = map(int,input().split())

print('Bus' if A<B else 'Subway' if A>B else 'Anything')