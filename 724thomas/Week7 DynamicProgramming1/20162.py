# https://www.acmicpc.net/problem/20162

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

from collections import defaultdict
def solution(n, arr):
    dp = [0 for _ in range(n)]

    for curr in range(n):
        dp[curr] = arr[curr]
        for prev in range(curr):
            if arr[prev] < arr[curr]:
                dp[curr] = max(dp[curr], dp[prev] + arr[curr])
    return max(dp)

if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(int(input()))
    print(solution(n, arr))
