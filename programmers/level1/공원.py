"""
Programmers Level 1

문제: 공원
"""

def is_possible(park, curr, size):
    x, y = curr
    possible = True
    for i in range(size):
        for j in range(size):
            if x + i >= len(park) or y + j >= len(park[0]) or park[x + i][y + j] != "-1":
                possible = False
                break
    return possible

def solution(mats, park):
    for mat in sorted(mats, reverse=True):
        for i in range(len(park)):
            for j in range(len(park[0])):
                if is_possible(park, [i, j], mat):
                    return mat
    return -1