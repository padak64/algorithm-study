"""
Programmers Level 1

문제: 추억 점수
"""

def solution(name, yearning, photos):
    answer = []
    persons = dict()
    for i, n in enumerate(name):
        persons[n] = yearning[i]

    for photo in photos:
        point=0
        for p in photo:
            if p in persons:
                point += persons[p]
        answer += [point]
                    
    return answer
