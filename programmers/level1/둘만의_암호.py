"""
Programmers Level 1

문제: 둘만의 암호
"""

def solution(s, skip, index):
    answer = ''
    alpha_list = list(chr(i) for i in range(ord("a"),ord("z")+1) if chr(i) not in skip)
    for i in s:
        answer += alpha_list[(alpha_list.index(i) + index) % len(alpha_list)]
    return answer