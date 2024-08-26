# https://www.acmicpc.net/problem/13699

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
    dp = [0] * (n+1)
    dp[0] = 1
    for j in range(1, n+1):
        dp[j] = sum([dp[i] * dp[j-i-1] for i in range(j)])
    return dp[-1]

n = int(input())
print(solution(n))


