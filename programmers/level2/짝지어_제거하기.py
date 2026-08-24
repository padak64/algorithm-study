"""
Programmers Level 2

문제: 짝지어 제거하기
"""

def solution(s):
    stack = []
    for ss in s:
        if ss in stack and stack[-1] == ss:
            stack.pop()
        else:
            stack.append(ss)
    return int(not stack)