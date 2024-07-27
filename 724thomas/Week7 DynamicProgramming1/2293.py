# https://www.acmicpc.net/problem/2293

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
    # dp 배열 초기화
    dp = [0] * (k + 1)
    dp[0] = 1

    # 각 동전에 대해 dp 배열 업데이트
    for coin in coins:
        for j in range(coin, k + 1):
            dp[j] += dp[j - coin]
    return dp[k]

if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    print(solution(n, k, coins))

