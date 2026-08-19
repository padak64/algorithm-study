"""
Programmers Level 1

문제: Bandaging
"""

def solution(bandage, health, attacks):
    attack_dict = {a[0]: a[1] for a in attacks}
    count = 0
    limit = health
    for t in range(attacks[-1][0] + 1):
        if attack_dict.get(t, 0) != 0:
            health -= attack_dict[t]
            count = 0
        else:
            health += bandage[1]
            count += 1
        if count == bandage[0]:
            health += bandage[2]
            count = 0
        if health <= 0 :
            return -1
        elif health > limit:
            health = limit
    return health