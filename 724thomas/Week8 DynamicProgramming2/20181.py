# https://www.acmicpc.net/problem/20181

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, k, arr):
    dp = [0] * (n + 1)
    total = 0
    left = 0
    result = 0

    for right in range(n):
        total += arr[right]

        while total >= k:
            dp[right + 1] = max(dp[right + 1], dp[left] + total - k)
            total -= arr[left]
            left += 1
        dp[right + 1] = max(dp[right + 1], dp[right])
        result = max(result, dp[right + 1])

    return result

if __name__ == '__main__':
    n, k = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(solution(n, k, arr))
