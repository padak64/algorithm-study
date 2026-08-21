"""
Programmers Level 1

문제: A Correct Parenthesis
"""

def solution(s):
    count = 0
    for ss in s:
        if ss == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    return count == 0