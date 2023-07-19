"""1436.py
영화감독 숌
https://www.acmicpc.net/problem/1436
"""

num = '666'
fast_digit = 0
cnt = 0
N = int(input())

while True:
    num = str(fast_digit)+'666'

    idx = num.find('6666')
    if idx == -1:
        cnt+=1
    
    else:
        total_len = len(num)
        idx+=3
        last_len = total_len-idx
        for i in range(10**last_len):
            cnt+=1
            if cnt==N:
                num= num[:idx]+(str(i).zfill(last_len))
                break 
    if cnt == N:
        break
    fast_digit+=1

print(int(num))