"""
Programmers Level 1

문제: 데이터 분석
"""

def solution(data, ext, val_ext, sort_by):
    name_list = ["code", "date", "maximum", "remain"]
    idx = name_list.index(ext)
    sort_idx = name_list.index(sort_by)
    my_dict = {}
    for d in data:
        if d[idx] < val_ext:
            my_dict.setdefault(d[sort_idx], []).append(d)
    result = []
    for d in sorted(my_dict):
        result.extend(my_dict[d])
    return result