"""
Programmers Level 1

문제: 시저 암호
"""

def solution(s, n):
    answer = ""
    upper_list = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    lower_list = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    for a in s:
        if a == " ":
            answer += " "
        elif a in upper_list:
            a_index = ord(a) - ord("A")
            answer += upper_list[(a_index + n) % len(upper_list)]
        elif a in lower_list:
            a_index = ord(a) - ord("a")
            answer += lower_list[(a_index + n) % len(lower_list)]
    return answer