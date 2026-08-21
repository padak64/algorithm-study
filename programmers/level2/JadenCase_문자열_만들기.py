"""
Programmers Level 2

문제: JadenCase 문자열 만들기
"""

def solution(s):
    answer = []
    for word in s.split(" "):
        if word:
            answer.append((word[0].upper() if word[0].islower() else word[0]) + word[1:].lower())
        else:
            answer.append("")        
    return " ".join(answer)