"""
Programmers Level 2

문제: 다음 큰 숫자
"""

def count_one(n):
    return bin(n)[2:].count("1")

def solution(n):
    count_n = count_one(n)
    while True:
        n += 1
        if count_n == count_one(n):
            return n