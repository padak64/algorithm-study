"""
Programmers Level 1

문제: 택배 상자 꺼내기
"""

def solution(n, w, num):
    answer = 0
    hh = n // w + 1 if n % w else n // w
    ww = -1
    for h in range(hh):
        line_list = [r if r <= n else 0 for r in range(h * w + 1, h * w + 1 + w)]
        if h % 2:
            line_list = line_list[::-1]
        if num in line_list:
            ww = line_list.index(num)
        if ww >= 0 and line_list[ww]:
            answer += 1
    return answer