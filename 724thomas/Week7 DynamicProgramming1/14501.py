# https://www.acmicpc.net/problem/14501

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr):
    print(arr)
    dp = [0] * (n+1)
    for i in range(n-1,-1,-1):
        t, p = arr[i]
        if i + t <= n:
            dp[i] = max(p + dp[i+t], dp[i+1])
        else:
            dp[i] = dp[i+1]
        print(dp)
    return dp[0]

n = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(n)]
print(solution(n, arr))


