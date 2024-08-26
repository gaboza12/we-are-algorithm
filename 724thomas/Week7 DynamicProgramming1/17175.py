# https://www.acmicpc.net/problem/17175

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n):
    if n <= 1:
        return 1
    if n == 2:
        return 3
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n+1):
        dp[i] = 1 + dp[i-1] + dp[i-2]
    return dp[n] % 1000000007


n = int(input())
print(solution(n))


