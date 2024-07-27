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


def solution(n):
    if n == 1:
        return 10

    dp = [[0] * 10 for _ in range(n)]

    for i in range(10):
        dp[0][i] = 1
    for i in range(n):
        dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, 10):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] if j > 0 else dp[i - 1][j]
    return 1


if __name__ == '__main__':
    print(solution(int(input())))
