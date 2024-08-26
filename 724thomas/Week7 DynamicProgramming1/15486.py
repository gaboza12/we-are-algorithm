# https://www.acmicpc.net/problem/15486

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


def solution(n, arr):
    dp = [0] * (n+1)
    for i in range(n - 1, -1, -1):
        days, cost = arr[i]
        if i + days <= n:
            dp[i] = max(dp[i+1], dp[i + days] + cost)
        else:
            dp[i] = dp[i+1]
    return dp[0]


if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(solution(n, arr))
