# https://www.acmicpc.net/problem/1890

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, grid):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1

    for row in range(n):
        for col in range(n):
            if dp[row][col] != 0 and grid[row][col] != 0:
                jump = grid[row][col]

                if row + jump < n:
                    dp[row+jump][col] += dp[row][col]
                if col + jump < n:
                    dp[row][col+jump] += dp[row][col]

    return dp[-1][-1]
n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().strip().split())))
print(solution(n, grid))
