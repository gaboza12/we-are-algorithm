# https://www.acmicpc.net/problem/2839

'''
1. 아이디어 :
    dp
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
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    return dp[n] if dp[n] != float('inf') else -1


n = int(input())
print(solution(n))
