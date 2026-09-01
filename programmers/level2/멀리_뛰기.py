"""
Programmers Level 2

문제: 멀리 뛰기
"""

def solution(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(2, n):
        a, b = b, (a + b) % 1234567
    return b