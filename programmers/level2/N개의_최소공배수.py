"""
Programmers Level 2

문제: N개의 최소공배수
"""

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return int((a * b) / gcd(a, b))

def solution(arr):
    answer = lcm(arr[0], arr[1])
    for a in arr[1:]:
        answer = lcm(answer, a)
    return answer

# def solution(arr):
#     answer = 1
#     num_list = arr
#     is_possible = True

#     while is_possible:
#         is_possible = False
#         for i in range(2, max(num_list) + 1):
#             cd_count = 0
#             n_list = []
#             for j in num_list:
#                 if j % i:
#                     n_list.append(j)
#                 else:
#                     cd_count += 1
#                     n_list.append(int(j / i))
#             if cd_count >= 2:
#                 answer *= i
#                 num_list = n_list
#                 is_possible = True
#                 break

#     for n in num_list:
#         answer *= n
#     return answer