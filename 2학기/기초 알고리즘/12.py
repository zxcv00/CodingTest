# 12. 해당 날짜가 무슨 요일인지 구하기
# ex) 21/10/14가 무슨 요일인지? | 21/1/1 금요일

import datetime

def get_days(yyyy, mm, dd):
    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return days[datetime.date(yyyy, mm, dd).weekday()]

y = 2021
m = 10
d = 14

print(f'{y}년 {m} 월 {d} 일 => {get_days(2021, 10, 14)}')

