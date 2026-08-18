"""
Programmers Level 1

문제: 공원 산책
"""

def solution(park, routes):
    dd = {"N": [-1, 0], "S": [1, 0], "W": [0, -1], "E": [0, 1]}

    for x_i, x in enumerate(park):
        for y_i, y in enumerate(x):
            if y == "S":
                start = [x_i, y_i]
                curr = start

    for route in routes:
        dir, dis = route.split()
        [curr_y, curr_x] = curr
        for _i in range(int(dis)):
            [curr_y, curr_x] = [sum(x) for x in zip([curr_y, curr_x], dd[dir])]
            if curr_y >= len(park) or curr_y < 0 or curr_x >= len(park[0]) or curr_x < 0 or park[curr_y][curr_x] == "X":
                [curr_y, curr_x] = curr
                break
        curr = [curr_y, curr_x]

    return curr