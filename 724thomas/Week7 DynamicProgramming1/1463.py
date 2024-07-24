# https://www.acmicpc.net/problem/1463

'''
1. 아이디어 :
    dp로 끝에서부터 연산을 시작한다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n):
    dp = [float('inf')] * (n + 1)
    dp[n] = 0
    for i in range(len(dp) - 2, 0, -1):
        dp[i] = min(dp[i], dp[i + 1] + 1)
        if i * 2 < len(dp):
            dp[i] = min(dp[i], dp[i * 2] + 1)
        if i * 3 < len(dp):
            dp[i] = min(dp[i], dp[i * 3] + 1)
    return dp[1]


n = int(input())
print(solution(n))
