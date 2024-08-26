# https://www.acmicpc.net/problem/10942

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, arr, queries):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            dp[i][i+1] = 1

    for length in range(3, n + 1):
        for start in range(n - length + 1):
            end = start + length - 1
            if arr[start] == arr[end] and dp[start+1][end-1]:
                dp[start][end] = 1

    for s, e in queries:
        print(dp[s-1][e-1])



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    q = []
    for _ in range(int(input())):
        q.append(list(map(int, input().strip().split())))
    solution(n, arr, q)
