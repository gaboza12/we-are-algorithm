# https://www.acmicpc.net/problem/22869

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, k, stones):
    dp = [0] * n
    dp[0] = 1

    for i in range(n):
        if not dp[i]:
            continue

        for j in range(i + 1, n):
            if (j - i) * (1 + abs(stones[i] - stones[j])) <= k:
                dp[j] = 1
    return "YES" if dp[n-1] == 1 else "NO"



n, k = list(map(int, input().strip().split()))
stones = list(map(int, input().strip().split()))
print(solution(n, k, stones))
