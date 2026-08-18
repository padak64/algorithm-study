"""
Programmers Level 1

문제: 성격 유형 검사하기
"""

def solution(survey, choices):
    answer = ''
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    part = ["RT", "CF", "JM", "AN"]

    for i in range(len(survey)):
        if choices[i] < 4:
            score[survey[i][0]] += (4 - choices[i])
        elif choices[i] > 4:
            score[survey[i][1]] += (choices[i] - 4)

    for p in part:
        if score[p[0]] >= score[p[1]]:
            answer += p[0]
        else:
            answer += p[1]

    return answer