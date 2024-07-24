# https://www.acmicpc.net/problem/9465

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr):
    if n == 1:
        return max(arr[0][0], arr[1][0])
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    dp[0][1] = dp[1][0] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]

    return max(max(dp[0]), max(dp[1]))

for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))


