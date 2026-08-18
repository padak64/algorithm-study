"""
Programmers Level 1

문제: 개인정보 수집 유효기간
"""

def translate_date(today):
    [year, month, day] = map(int, today.split("."))
    return (year * 12 * 28) + (month * 28) + day

def solution(today, terms, privacies):
    answer = []
    terms_dict = {t.split()[0]: int(t.split()[1]) for t in terms}
    today_d = translate_date(today)

    for idx, privacy in enumerate(privacies):
        [start, property] = privacy.split()
        start_d = translate_date(start)
        if today_d - start_d >= terms_dict[property] * 28:
            answer.append(idx + 1)

    return answer