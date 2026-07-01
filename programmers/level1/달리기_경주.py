"""
Programmers Level 1

문제: 달리기 경주
"""

def solution(players, callings):
    dict={player: i for i, player in enumerate(players)}

    for curr_player in callings:
        curr_index=dict[curr_player]
        front_index=curr_index-1

        front_player=players[front_index]

        players[front_index], players[curr_index] = players[curr_index], players[front_index]

        dict[curr_player], dict[front_player] = front_index, curr_index

    return players