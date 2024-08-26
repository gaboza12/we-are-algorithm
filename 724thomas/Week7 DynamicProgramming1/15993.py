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

def solution(arr):
    MOD = 1000000009
    n = max(arr)

    dp = [[0, 0] for _ in range(n+1)]

    dp[1][0] = 1
    dp[2][0] = 1
    dp[2][1] = 1
    dp[3][0] = 2
    dp[3][1] = 2


    for i in range(4, n+1):
        dp[i][0] = (dp[i-1][1] + dp[i-2][1] + dp[i-3][1]) % MOD
        dp[i][1] = (dp[i-1][0] + dp[i-2][0] + dp[i-3][0]) % MOD


    for i in arr:
        print(*dp[i])

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append(int(input()))
    solution(arr)


