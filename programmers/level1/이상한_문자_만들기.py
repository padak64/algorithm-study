"""
Programmers Level 1

문제: 이상한 문자 만들기
"""

def solution(s):
    answer = ''
    start_new_word = 0
    for idx in range(len(s)):
        if s[idx] == ' ':
            start_new_word = idx + 1
            answer += ' '
        else:
            i = idx - start_new_word
            if i % 2:
                answer += s[idx].lower()
            else:
                answer += s[idx].upper()
    return answer