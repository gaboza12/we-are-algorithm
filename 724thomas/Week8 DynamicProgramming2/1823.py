# https://www.acmicpc.net/problem/1823

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

from collections import deque, defaultdict

def solution(n, arr):
    # DP 테이블 초기화
    dp = [[0] * n for _ in range(n)]

    # 단일 밭의 밀 수확량 초기화
    for i in range(n):
        dp[i][i] = arr[i] * n

    # 두 밭 이상의 경우 계산
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            year = n - length + 1
            dp[left][right] = max(dp[left + 1][right] + arr[left] * year, dp[left][right - 1] + arr[right] * year)
    return dp[0][n - 1]


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    print(solution(n, arr))
