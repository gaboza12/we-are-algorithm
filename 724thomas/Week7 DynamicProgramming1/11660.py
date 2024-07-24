# https://www.acmicpc.net/problem/11660

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, graph, cords):
    dp = [[0 for i in range(n+1)] for _ in range(n+1)]
    dp[1][1] = graph[0][0]
    for i in range(1, n+1):
        dp[i][1] = dp[i - 1][1] + graph[i-1][0]
        dp[1][i] = dp[1][i - 1] + graph[0][i-1]

    for row in range(2, n+1):
        for col in range(2, n+1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + graph[row-1][col-1]

    for r1, c1, r2, c2 in cords:
        val = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]
        print(val)

n, m = list(map(int, input().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
cords = []
for _ in range(m):
    cords.append((list(map(int, input().split()))))
solution(n, m, graph, cords)
