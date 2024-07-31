# https://www.acmicpc.net/problem/11049

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
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n):  # 행렬 체인의 길이
        for left in range(n - length):  # 시작 지점
            right = left + length
            dp[left][right] = float('inf')
            for k in range(left, right):
                cost = dp[left][k] + dp[k + 1][right] + arr[left][0] * arr[k][1] * arr[right][1]
                dp[left][right] = min(dp[left][right], cost)

    print(*dp, sep='\n')
    return dp[0][n - 1]


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    print(solution(n, arr))
