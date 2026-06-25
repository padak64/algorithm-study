"""
Programmers Level 1

문제: 노란불 신호등
"""

import math

def solution(signals):
    sums = [sum(row) for row in signals]

    # 넉넉하게 첫 교집합을 찾을 수 있도록 범위 설정
    limit = math.lcm(*sums) * 2 

    arr = []
    for index, [g, y, r] in enumerate(signals):
        y_set = set() # 검색 속도를 극대화하기 위해 set 사용
        i = g  # 0초 기준으로 시작 지점 잡기

        while i < limit:
            # 0초 기준의 시간대들을 집합에 추가
            for second in range(i, i + y):
                y_set.add(second)
            i += sums[index]

        arr.append(y_set)

    # 모든 신호등의 노란불 시간대 교집합 구하기
    common_seconds = arr[0]
    for s in arr[1:]:
        common_seconds &= s # 교집합 연산 (&)

    if common_seconds:
        # 공통 시간 중 가장 빠른 시간(0초 기준)을 찾은 뒤 + 1 (1번째 초 기준으로 변환)
        return min(common_seconds) + 1

    return -1

