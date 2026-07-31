"""
Programmers Level 1

문제: 숫자 짝꿍
"""

def solution(X, Y):
    answer = ""
    x_dict, y_dict = {}, {}
    for x in X:
        x_dict[x] = x_dict.get(x, 0) + 1
    for y in Y:
        y_dict[y] = y_dict.get(y, 0) + 1

    for i in sorted(x_dict, reverse=True):
        if i in y_dict:
            answer += str(i) * min(x_dict[i], y_dict[i])

    if answer == "":
        return "-1"
    elif answer[0] == "0":
        return "0"
    else:
        return answer