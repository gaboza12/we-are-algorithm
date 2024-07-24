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

MOD = 1000000007


def solution(n):
    if n == 1:
        return 2
    if n == 2:
        return 7
    if n == 3:
        return 22
    dp = list(0 for _ in range(n + 1))
    dp[0] = 1
    dp[1] = 2
    dp[2] = 7

    for i in range(3, n + 1):
        dp[i] = (3 * dp[i - 1] + dp[i - 2] - dp[i - 3]) % 1000000007
    return dp[n]

if __name__ == '__main__':
    print(solution(int(input())))
