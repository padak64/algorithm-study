"""
Programmers Level 1

문제: 방의 개수
"""

def solution(arrows):
    answer = 0
    a = {0: [0, 1], 1: [1, 1], 2: [1, 0], 3: [1, -1], 4: [0, -1], 5: [-1, -1], 6: [-1, 0], 7: [-1, 1]}
    curr = (0, 0)
    dots = set()
    dots.add(curr)
    lines = set()

    for arrow in arrows:
        for _i in range(2):
            x, y = curr
            x2, y2 = a[arrow]
            curr = (x + x2, y + y2)
            if curr in dots:
                if((x, y), curr) not in lines and (curr, (x, y)) not in lines:
                    answer += 1
            dots.add(curr)
            lines.add(((x, y), curr))
            
    return answer