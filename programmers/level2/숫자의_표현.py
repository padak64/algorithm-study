"""
Programmers Level 2

문제: 숫자의 표현
"""

def solution(n):
    answer = 0
    for i in range(1, n):
        for j in range(i, n):
            if (sum_n := sum(range(i, j + 1))) == n:
                answer += 1
            elif sum_n > n:
                break
    return answer + 1