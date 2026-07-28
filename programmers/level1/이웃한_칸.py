"""
Programmers Level 1

문제: 이웃한 칸
"""

def solution(board, h, w):
    answer = 0
    len_b = len(board)
    h_list = [-1, 0, 0, 1]
    w_list = [0, -1, 1, 0]
    for i in range(4):
        hh = h + h_list[i]
        ww = w + w_list[i]
        if 0 <= hh < len_b and 0 <= ww < len_b:
            if board[h][w] == board[hh][ww]:
                answer += 1
    return answer