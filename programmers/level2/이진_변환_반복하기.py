"""
Programmers Level 2

문제: 이진 변환 반복하기
"""

def solution(s):
    count_zero, count = 0, 0
    while s != "1":
        len_no_zero = len("".join(s.split("0")))
        count_zero += len(s) - len_no_zero
        count += 1
        s = bin(len_no_zero)[2:]
    return [count, count_zero]