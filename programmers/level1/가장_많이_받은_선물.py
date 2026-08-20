"""
Programmers Level 1

문제: 가장 많이 받은 선물
"""

def solution(friends, gifts):
    pingpong = {}
    for friend in friends:
        pingpong[friend] = {f: 0 for f in friends}

    for gift in gifts:
        sender, receiver = gift.split()
        pingpong[sender][receiver] += 1

    count = {}
    for friend in friends:
        send = sum(pingpong[friend].values())
        receive = sum(value[friend] for _key, value in pingpong.items())
        score = send - receive
        count[friend] = score

    gift_count = {f: 0 for f in friends}
    for a_idx, a in enumerate(friends):
        for b in friends[a_idx + 1:]:
            ab = pingpong[a][b]
            ba = pingpong[b][a]
            if ab + ba == 0 or ab == ba:
                if count[a] != count[b]:
                    gift_count[a if count[a] > count[b] else b] += 1
            else:
                gift_count[a if ab > ba else b] += 1

    return max(gift_count.values())