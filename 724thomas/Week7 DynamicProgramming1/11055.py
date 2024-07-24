# https://www.acmicpc.net/problem/11055

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
    dp = [arr[i] for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[j] + arr[i], dp[i])
    return max(dp)


n = int(input())
arr = list(map(int, input().strip().split()))

print(solution(n, arr))
