# https://www.acmicpc.net/problem/9084

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

def solution(n, coins, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, target+1):
            dp[i] += dp[i-coin]

    return dp[-1]

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        coins = list(map(int, input().strip().split()))
        target = int(input())
        print(solution(n, coins, target))


