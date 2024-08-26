# https://www.acmicpc.net/problem/1082

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, money, prices):

    dp = [-float('inf')] * (money+1)
    for i in range(n-1, -1, -1):
        price = prices[i]
        for j in range(price, money+1):
            dp[j] = max(dp[j], i, dp[j-price] * 10 + i)
    return dp[money]

n = int(input())
arr = list(map(int, input().strip().split()))
m = int(input())
print(solution(n, m, arr))
