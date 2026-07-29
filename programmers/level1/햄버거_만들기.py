"""
Programmers Level 1

문제: 햄버거 만들기
"""

def solution(ingredient):
    answer = 0
    i_list = []
    for i in ingredient:
        i_list.append(i)
        if i_list[-4:] == [1,2,3,1]:
            i_list.pop()
            i_list.pop()
            i_list.pop()
            i_list.pop()
            answer += 1
    return answer