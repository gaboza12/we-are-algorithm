# https://www.acmicpc.net/problem/

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

def solution(arr):
    MOD = 1000000009
    n = m = 0
    for cn, cm in arr:
        n = max(n, cn)
        m = max(m, cm)

    dp = [[0 for _ in range(m+1)] for _ in range(n+2)]
    dp[1][1] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    dp[3][1] = 1
    dp[3][2] = 2
    dp[3][3] = 1

    for i in range(4, n+1):
        for j in range(1, m+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % MOD

    print(*dp, sep="\n")

    for cn, cm in arr:
        print((dp[cn][cm]) % MOD)

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(int, input().strip().split())))
    solution(arr)


