# https://www.acmicpc.net/problem/15991

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, arr):
    max_n = max(arr)
    dp = [0] * (max_n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2
    dp[4] = 3

    for i in range(5, max_n+1):
        dp[i] = dp[i-2] % 1000000009+ dp[i-4] % 1000000009 + dp[i-6] % 1000000009
    ans = []
    for n in arr:
        print(dp[n]  % 1000000009)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    solution(n, arr)
