# https://www.acmicpc.net/problem/

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


def solution(n, m, k):
    dp = [[0] * m for _ in range(n)]

    if k == 0:
        # k가 0이면 끝점까지 한번에 가야 함
        for row in range(n):
            dp[row][0] = 1
        for col in range(m):
            dp[0][col] = 1

        for row in range(1, n):
            for col in range(1, m):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]

    # k의 위치 계산
    mid_x = (k - 1) // m
    mid_y = (k - 1) % m

    # 초기 경로 설정
    for row in range(mid_x + 1):
        dp[row][0] = 1
    for col in range(mid_y + 1):
        dp[0][col] = 1

    # mid 지점까지의 경로 수 계산
    for row in range(1, mid_x + 1):
        for col in range(1, mid_y + 1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    # 중간 지점에서 끝점까지의 경로 수 계산
    for row in range(mid_x, n):
        dp[row][mid_y] = dp[mid_x][mid_y]
    for col in range(mid_y, m):
        dp[mid_x][col] = dp[mid_x][mid_y]

    for row in range(mid_x + 1, n):
        for col in range(mid_y + 1, m):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

    return dp[-1][-1]


if __name__ == '__main__':
    n, m, k = list(map(int, input().strip().split()))
    print(solution(n, m, k))

