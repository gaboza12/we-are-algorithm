# https://www.acmicpc.net/problem/17212

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n):

    coins = [1,2,5,7]
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, n+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[-1]


print(solution(int(input())))


