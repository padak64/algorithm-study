"""
Programmers Level 2

문제: 카펫
"""

def solution(brown, yellow):
    all = brown + yellow
    for i in range(3, all // 3 + 1):
        if all % i == 0 and (i - 2) * (all // i - 2) == yellow:
            return sorted([i, all // i], reverse=True)