"""
Programmers Level 1

문제: 직사각형 별찍기
"""

a, b = map(int, input().strip().split(' '))
for i in range(b):
    print("*" * a)