"""
Programmers Level 2

문제: 구명보트
"""

from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        if len(people) > 1 and people[0] + people[-1] <= limit:
            people.popleft()
        people.pop()
        answer += 1
    return answer