"""
Programmers Level 2

문제: 연속 부분 수열 합의 개수
"""

def solution(elements):
    e_len = len(elements)
    nums = set()
    for i in range(1, e_len + 1):
        for j in range(e_len):
            if j + i > e_len:
                nums.add(sum(elements[j:] + elements[:j + i - e_len]))
            else:
                nums.add(sum(elements[j:j+i]))
    return len(nums)