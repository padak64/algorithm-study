"""
Programmers Level 2

문제: 최댓값과 최솟값
"""

def solution(s):
    ss = list(map(int, s.split()))
    return str(min(ss)) + " " + str(max(ss))