"""
Programmers Level 1

문제: 자연수 뒤집어 배열로 만들기
"""

def solution(n):
    return [int(i) for i in str(n)[::-1]]