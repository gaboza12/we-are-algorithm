# https://www.acmicpc.net/problem/1669

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(X, Y):
    if X == Y:
        return 0

    diff = Y - X
    day = 0

    for i in range(1, 2 ** 31):
        for _ in range(2):
            if diff <= 0:
                return day
            day += 1
            diff -= i

a, b = list(map(int, input().split()))
print(solution(a, b))