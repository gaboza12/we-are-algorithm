# https://www.acmicpc.net/problem/15989

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):
    cmax = max(arr)
    dp = [0] * (cmax+1)
    dp[0] = 1

    for num in range(1,4):
        for i in range(num, cmax+1):
            dp[i] += dp[i-num]
    for n in arr:
        print(dp[n])


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    solution(n, arr)

