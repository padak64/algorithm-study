"""
Programmers Level 2

문제: 점프와 순간 이동
"""

def solution(n):
    ans = 0
    while n:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n /= 2
    return ans