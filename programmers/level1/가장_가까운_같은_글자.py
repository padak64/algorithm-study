"""
Programmers Level 1

문제: 가장 가까운 같은 글자
"""

def solution(s):
    answer = []
    dict = {}
    for idx, i in enumerate(s):
        if i in dict:
            answer.append(idx - dict[i])
        else:
            answer.append(-1)
        dict[i] = idx
    return answer