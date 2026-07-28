"""
Programmers Level 1

문제: 문자열 나누기
"""

def solution(s):
    answer = 0
    x, y = 0, 0
    x_idx = 0
    for i in range(len(s)):
        if s[i] == s[x_idx]:
            x += 1
        else:
            y += 1
        if x == y:
            x, y = 0, 0
            x_idx = i + 1
            answer += 1
    if x_idx != len(s):
        answer += 1
    return answer