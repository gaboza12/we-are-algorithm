# https://www.acmicpc.net/problem/17485

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


def solution(n, m, arr):
    dp = [[[float('inf'), float('inf'), float('inf')] for _ in range(m)] for _ in range(n)]

    for col in range(m):
        for i in range(3):
            dp[0][col][i] = arr[0][col]  # from left, mid, right

    for row in range(1, n):
        for col in range(m):
            val = arr[row][col]
            if col == 0:
                dp[row][col][1] = min(dp[row - 1][col][0], dp[row - 1][col][2]) + val  # from up
                dp[row][col][2] = min(dp[row - 1][col + 1][0], dp[row - 1][col + 1][1]) + val  # from right-up
            elif col == m - 1:
                dp[row][col][0] = min(dp[row - 1][col - 1][1], dp[row - 1][col - 1][2]) + val  # from left-up
                dp[row][col][1] = min(dp[row - 1][col][0], dp[row - 1][col][2]) + val  # from up
            else:
                dp[row][col][0] = min(dp[row - 1][col - 1][1], dp[row - 1][col - 1][2]) + val  # from left-up
                dp[row][col][1] = min(dp[row - 1][col][0], dp[row - 1][col][2]) + val  # from up
                dp[row][col][2] = min(dp[row - 1][col + 1][0], dp[row - 1][col + 1][1]) + val  # from right-up
        print(*dp, sep='\n')
        print()
    ans = float('inf')
    for col in dp[-1]:
        ans = min(ans, min(col))
    return ans


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, m, arr))
