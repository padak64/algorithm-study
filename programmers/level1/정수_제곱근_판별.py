"""
Programmers Level 1

문제: 정수 제곱근 판별
"""

def solution(n):
    if (x := (n ** 0.5)).is_integer():
        return (x + 1) ** 2
    return -1