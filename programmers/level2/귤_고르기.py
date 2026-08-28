"""
Programmers Level 2

문제: 귤 고르기
"""

def solution(k, tangerine):
    answer = 0
    dict_t = {i: 0 for i in set(tangerine)}
    for i in tangerine:
        dict_t[i] += 1
    for t in sorted(dict_t.values(), reverse=True):
        k -= t
        answer += 1
        if k <= 0:
            break
    return answer