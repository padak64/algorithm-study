"""
Programmers Level 1

문제: 덧칠하기
"""

def solution(n, m, section):
    result = 0
    paint_area = 0
    for s in section:
        if s > paint_area:
            result += 1
            paint_area = s + m - 1
    return result

