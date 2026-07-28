"""
Programmers Level 1

문제: 콜라 문제
"""

def solution(a, b, n):
    answer = 0
    while n >= a:
        return_bottle = (n // a) * b
        remain_bottle = n % a
        n = return_bottle + remain_bottle
        answer += return_bottle
    return answer