"""
Programmers Level 1

문제: 푸드 파이트 대회
"""

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (int(food[i]) // 2)
    return "0".join([answer, answer[::-1]])