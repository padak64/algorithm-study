"""
Programmers Level 1

문제: 바탕화면 정리
"""

def solution(wallpaper):
    lux, luy, rux, ruy = -1, -1, -1, -1
    for w in range(len(wallpaper)):
        if "#" in wallpaper[w]:
            if lux == -1:
                lux = w
            if rux < w:
                rux = w
            for h in range(len(wallpaper[w])):
                if wallpaper[w][h] == "#":
                    if luy == -1 or luy > h:
                        luy = h
                    if ruy < h:
                        ruy = h
    return [lux, luy, rux + 1, ruy + 1]