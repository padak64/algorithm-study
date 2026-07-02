"""
Programmers Level 1

문제: 유연근무제
"""

def is_safe(schedule, timelog, weekday):
    if weekday:
        return timelog - schedule <= 10
    else:
        return True

def solution(schedules, timelogs, startday):
    answer = 0
    weekday = list(i % 7 not in [6,0] for i in range(startday, startday + 7))

    for i in range(len(schedules)):
        schedule = schedules[i] if schedules[i] % 100 < 50 else schedules[i] + 40
        if all(is_safe(schedule, timelogs[i][j], weekday[j]) for j in range(7)):
            answer += 1

    return answer
