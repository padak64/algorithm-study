"""
Programmers Level 1

문제: 중요한 단어를 스포 방지
"""

def solution(message, spoiler_ranges):
    answer = 0
    spoiler_list = set()
    normal_message = message

    for a, b in spoiler_ranges:
        # 1. 왼쪽으로 가며 가장 가까운 공백의 '다음 칸' 찾기 (단어 시작점)
        start_space = message[:a].rfind(' ')
        start_index = start_space + 1 if start_space != -1 else 0

        # 2. b번 인덱스부터 오른쪽으로 가며 공백 찾기 (단어 끝점)
        end_index = message.find(' ', b)
        if end_index == -1:
            end_index = len(message)

        # 3. 단어 추출 및 마스킹 (공백으로 채워 인덱스 보존)
        spoiler_word = message[start_index:end_index]
        spoiler_list.update(spoiler_word.split())
        
        normal_message = normal_message[:start_index] + ' ' * len(spoiler_word) + normal_message[end_index:]

    # 4. 일반 구간 단어들과 비교해서 카운트
    normal_words = normal_message.split()
    for spoiler_word in spoiler_list:
        if spoiler_word not in normal_words:
            answer += 1

    return answer