# https://www.acmicpc.net/problem/2457

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque


def solution(flowers):
    flowers = deque(sorted(flowers))
    count, end, target = 0, 0, 301

    while flowers:
        if target >= 1201 or target < flowers[0][0]:
            break
        for _ in range(len(flowers)):
            if target >= flowers[0][0]:
                end = max(end, flowers[0][1])
                flowers.popleft()
            else:
                break
        target = end
        count += 1

    return count if target >= 1201 else 0

n = int(input())
flowers = []
for _ in range(n):
    sm, sd, em, ed = list(map(int, input().strip().split()))
    flowers.append((sm * 100 + sd, em * 100 + ed))
print(solution(flowers))
