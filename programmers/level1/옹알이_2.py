"""
Programmers Level 1

문제: 옹알이 (2)
"""

def solution(babbling):
    answer = 0
    for b in babbling:
        for p in ["aya", "ye", "woo", "ma"]:
            if p * 2 not in b:
                b = b.replace(p, " ")
        if b.strip() == "":
            answer += 1
    return answer