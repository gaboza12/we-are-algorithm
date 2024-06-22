# https://www.acmicpc.net/problem/1002

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(arr):
    x1, y1, r1, x2, y2, r2 = arr

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if distance == 0 and r1 == r2:
        return -1
    if distance == r1 + r2 or distance == abs(r1 - r2):
        return 1
    if abs(r1 - r2) < distance < r1 + r2:
        return 2
    return 0

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    print(solution(arr))
