# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, k, coins):
    dp = [float('inf')] * (k+1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, k+1):
            dp[i] = min(dp[i], dp[i-coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1

if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    print(solution(n, k, coins))


