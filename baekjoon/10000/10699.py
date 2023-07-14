"""10699.py
오늘 날짜
https://www.acmicpc.net/problem/10699
"""

import datetime
# UTC 0 기준 tz 세팅
tz = datetime.timezone(datetime.timedelta(hours=9))
print(datetime.datetime.now(tz=tz).strftime("%Y-%m-%d"))