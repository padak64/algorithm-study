"""
Programmers Level 1

문제: 동영상 재생기
"""

def min_to_sec(min):
    m, s = min.split(":")
    return (int(m) * 60) + int(s)

def set_format(i):
    if i < 10:
        return "0" + str(i)
    return str(i)

def sec_to_min(sec):
    return set_format(sec // 60) + ":" + set_format(sec % 60)

def solution(video_len, pos, op_start, op_end, commands):
    video_len = min_to_sec(video_len)
    pos = min_to_sec(pos)
    op_start = min_to_sec(op_start)
    op_end = min_to_sec(op_end)

    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end

        if command == "prev":
            pos = pos - 10
        elif command == "next":
            pos = pos + 10

        if pos > video_len:
            pos = video_len
        elif op_start <= pos <= op_end:
            pos = op_end
        elif pos < 0:
            pos = 0

    return sec_to_min(pos)