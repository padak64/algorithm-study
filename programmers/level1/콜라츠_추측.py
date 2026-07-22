"""
Programmers Level 1

문제: 콜라츠 추측
"""

def solution(num):
    i = 0
    while i < 500:
        if num == 1:
            return 0 if i == 0 else i
        if num % 2:
            num = num * 3 + 1
        else:
            num = num / 2
        i += 1
    return -1
