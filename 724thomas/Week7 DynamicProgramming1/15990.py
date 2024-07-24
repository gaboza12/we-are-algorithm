# https://www.acmicpc.net/problem/15990

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(arr):
    cmax = max(5, max(arr)+1)
    dp = [[0] * 4 for _ in range(cmax)]
    dp[1][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1
    dp[4][1] = 2
    dp[4][3] = 1

    for i in range(5, cmax):
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009

    for n in arr:
        print(sum(dp[n]) % 1000000009)


arr = []
for _ in range(int(input())):
    arr.append(int(input()))
solution(arr)
