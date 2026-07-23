"""
Programmers Level 1

문제: 최대공약수와 최소공배수
"""

def solution(n, m):
    answer = []
    for i in range(max(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    n_list = [i for i in range(n, n * m + 1, n)]
    for i in range(m, n * m + 1, m):
        if i in n_list:
            answer.append(i)
            break
    return answer