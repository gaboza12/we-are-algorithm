# https://www.acmicpc.net/problem/10844

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n):
    dp = [1] * 10
    dp[0] = 0

    for _ in range(n-1):
        temp = [0] * 10
        for i in range(10):
            if i == 0:
                temp[1] += dp[0]
            elif i == 9:
                temp[8] += dp[9]
            else:
                temp[i-1] += dp[i]
                temp[i+1] += dp[i]
        dp = temp.copy()
    return sum(dp) % 1000000000


n = int(input())
print(solution(n))
