# https://www.acmicpc.net/problem/16195

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict


def solution(arr):
    n = 0
    m = 0
    for cn, cm in arr:
        n = max(n, cn)
        m = max(m, cm)

    dp = [[0 for _ in range(m)] for _ in range(n+1)]

    dp[1][0] = 1
    dp[2][0] = dp[2][1] = 1
    dp[3][0] = dp[3][2] = 1
    dp[3][1] = 2
    for dp_idx in range(3, n+1):
        for counts in range(1, m):
            dp[dp_idx][counts] = (dp[dp_idx - 1][counts - 1] + dp[dp_idx - 2][counts - 1] + dp[dp_idx - 3][
                counts - 1]) % 1000000009

    for cn, cm in arr:
        print(sum(dp[cn][:cm]) % 1000000009)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    solution(arr)

'''

4 3 = 3+1, 1+3, 2+2, 1+1+2, 1+2+1, 2+1+1
'''
