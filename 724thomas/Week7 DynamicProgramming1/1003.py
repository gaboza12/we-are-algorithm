# https://www.acmicpc.net/problem/1003

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
    n = max(arr)

    dp = [[0,0]] * (n+1)
    dp[0] = [1, 0]
    if n != 0:

        dp[1] = [0, 1]
        

        for i in range(2, n+1):
            zero = dp[i-2][0] + dp[i-1][0]
            ones = dp[i-2][1] + dp[i-1][1]
            dp[i] = [zero, ones]

    for n in arr:
        print(*dp[n])

arr = []
for _ in range(int(input())):
    arr.append(int(input()))
solution(arr)
