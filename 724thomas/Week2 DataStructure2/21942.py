# https://www.acmicpc.net/problem/21942

'''
1. 아이디어 :
    거지같은 문제
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    해시맵
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from datetime import datetime, timedelta
def solution(n, duration_str, fee_per_minute, logs):
    def parse_time(date_str, time_str):
        return datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")

    def parse_duration(duration_str):
        days, time_str = duration_str.split("/")
        hours, minutes = map(int, time_str.split(":"))
        return timedelta(days=int(days), hours=hours, minutes=minutes)


    def calculate_late_fee(borrow_time, return_time, duration, fee_per_minute):
        due_time = borrow_time + duration
        late_duration = return_time - due_time
        if late_duration.total_seconds() > 0:
            late_minutes = int(late_duration.total_seconds() // 60)
            return late_minutes * fee_per_minute
        return 0

    duration = parse_duration(duration_str)
    fee_per_minute = int(fee_per_minute)

    borrow_records = {}
    fees = {}

    for log in logs:
        date_str, time_str, part, user = log.strip().split()
        current_time = parse_time(date_str, time_str)

        if (part, user) in borrow_records:
            borrow_time = borrow_records.pop((part, user))
            late_fee = calculate_late_fee(borrow_time, current_time, duration, fee_per_minute)
            if late_fee > 0:
                if user in fees:
                    fees[user] += late_fee
                else:
                    fees[user] = late_fee
        else:
            borrow_records[(part, user)] = current_time

    if not fees:
        return -1
    else:
        result = []
        for user in sorted(fees.keys()):
            result.append(f"{user} {fees[user]}")
        return "\n".join(result)

n, duration_str, fee_per_minute = input().strip().split()
n = int(n)
logs = [input().strip() for _ in range(n)]
print(solution(n, duration_str, fee_per_minute, logs))