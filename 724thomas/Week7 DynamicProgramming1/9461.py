# https://www.acmicpc.net/problem/9461

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(arr):
    cmax = max(arr)
    dp = [0] * (cmax+1)
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2


    for i in range(5, cmax+1):
        dp[i] = dp[i-1] + dp[i-5]
    for n in arr:
        print(dp[n])


arr = []
for _ in range(int(input())):
    arr.append(int(input()))
solution(arr)


