# https://www.acmicpc.net/problem/2156

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
    dp = [0] * (n+1)
    if n == 1:
        return arr[0]

    arr = [0] + arr
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    return dp[-1]


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
print(solution(n, arr))


