# https://www.acmicpc.net/problem/2579

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    if n == 1:
        return arr[0]
    elif n == 2:
        return sum(arr)
    elif n == 3:
        return max(arr[0] + arr[2], arr[1] + arr[2])
    dp = [0] * (n+1)
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, len(arr)):
        dp[i] = max( dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i] )
    return dp[n-1]

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(solution(n, arr))
