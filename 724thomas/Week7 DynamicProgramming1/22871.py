# https://www.acmicpc.net/problem/22871

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
    dp = [float('inf')] * n
    dp[0] = 0

    for start in range(n):
        for end in range(start + 1, n):
            val = (end - start) * (1 + abs(arr[start] - arr[end]))
            dp[end] = min(dp[end], max(dp[start], val))

    return dp[-1]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))
