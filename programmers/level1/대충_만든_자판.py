"""
Programmers Level 1

문제: 대충 만든 자판
"""

def solution(keymap, targets):
    answer = []
    key_dict = {}
    for key in keymap:
        for k in range(len(key)):
            if key[k] in key_dict and key_dict[key[k]] > k + 1:
                key_dict[key[k]] = k + 1
            elif key[k] not in key_dict:
                key_dict[key[k]] = k + 1
    for target in targets:
        count = 0
        for a in target:
            if a in key_dict:
                count += key_dict[a]
            else:
                count = -1
                break
        answer.append(count)
    return answer