# https://www.acmicpc.net/problem/14430

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = grid[0][0]
    for row in range(1, n):
        dp[row][0] = dp[row-1][0] + grid[row][0]
    for col in range(1, m):
        dp[0][col] = dp[0][col-1] + grid[0][col]

    for row in range(1, n):
        for col in range(1, m):
            dp[row][col] = max(dp[row-1][col], dp[row][col-1]) + grid[row][col]

    return dp[-1][-1]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
    print(solution(n, m, grid))


