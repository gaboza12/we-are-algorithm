# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m):
    length = abs(n - m) + 1
    dp = [[0] * length for _ in range(length)]
    for col in range(length):
        dp[0][col] = 1

    for row in range(1, length):
        for col in range(1, length):
            if row > col:
                continue
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    return dp[-1][-1]


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    print(solution(n, m))
