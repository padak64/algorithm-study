"""
Programmers Level 1

문제: 지폐 접기
"""

def solution(wallet, bill):
    answer = 0
    wallet = [max(wallet), min(wallet)]
    bill = [max(bill), min(bill)]
    while bill[0] > wallet[0] or bill[1] > wallet[1]:
        bill = sorted([bill[0] // 2, bill[1]], reverse=True)
        answer += 1
    return answer