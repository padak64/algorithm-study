"""
Programmers Level 1

문제: 하샤드 수
"""

def solution(x):
    return False if x % sum(map(int, str(x))) else True