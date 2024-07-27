# https://www.acmicpc.net/problem/21317

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, one, two, k):
    if n == 1:
        return 0

    dp = [float('inf')] * n
    dp[0] = 0
    dp[1] = one[0]

    if n > 2:
        dp[2] = min(dp[1] + one[1], two[0])  # 세 번째 돌로 가는 비용

    for i in range(3, n):
        dp[i] = min(dp[i - 1] + one[i - 1], dp[i - 2] + two[i - 2])

    ans = dp[n - 1]

    for i in range(n - 3):
        big_jump_cost = dp[i] + k
        dp2 = [float('inf')] * n
        dp2[i + 3] = big_jump_cost

        for j in range(i + 4, n):
            dp2[j] = min(dp2[j - 1] + one[j - 1], dp2[j - 2] + two[j - 2])

        ans = min(ans, dp2[-1])

    return ans


n = int(input())
one = []
two = []
for _ in range(n - 1):
    a, b = list(map(int, input().strip().split()))
    one.append(a)
    two.append(b)
k = int(input())
print(solution(n, one, two, k))
