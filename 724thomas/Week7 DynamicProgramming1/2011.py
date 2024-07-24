# https://www.acmicpc.net/problem/2011

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


def solution(code):
    if not code or code[0] == "0":
        return 0

    n = len(code)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        single = int(code[i - 1:i])
        double = int(code[i - 2:i])

        if 1 <= single <= 9:
            dp[i] += dp[i - 1] % 1000000
        if 10 <= double <= 26:
            dp[i] += dp[i - 2] % 1000000
    return dp[n] % 1000000

if __name__ == '__main__':
    s = input().strip()
    print(solution(s))
