# https://www.acmicpc.net/problem/2225

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


def solution(n, k):
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    dp[0][0] = 1
    for i in range(n+1):
        for j in range(1, k+1):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
    return dp[-1][-1]


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    print(solution(n, m))
