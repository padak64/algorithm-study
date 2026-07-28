"""
Programmers Level 1

문제: 과일 장수
"""

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score) // m):
        answer += score[(m * i) + m - 1] * m
    return answer