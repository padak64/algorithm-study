"""
Programmers Level 1

문제: 명예의 전당 (1)
"""

def solution(k, score):
    answer = []
    legend = []
    for s in score:
        legend.append(s)
        legend.sort(reverse=True)
        if len(legend) > k:
            legend.pop()
        answer.append(legend[-1])
    return answer