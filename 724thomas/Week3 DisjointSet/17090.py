# https://www.acmicpc.net/problem/17090

'''
1. 아이디어 :
    dfs와 dp를 사용한다.
    visited와 escape에 각각 방문했는지에 대한 체크와 탈출가능한 여부를 저장한다.
2. 시간복잡도 :
    O( n*m )
3. 자료구조 :
    배열, 해시맵
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, graph):
    def dfs(row1, col1):
        if visited[row1][col1]:
            return escape[row1][col1]
        visited[row1][col1] = True

        row2, col2 = dirs[graph[row1][col1]]
        nrow, ncol = row1 + row2, col1 + col2

        if not (0 <= nrow < n and 0 <= ncol < m):
            escape[row1][col1] = True
        else:
            escape[row1][col1] = dfs(nrow, ncol)

        return escape[row1][col1]

    visited = [[False] * m for _ in range(n)]
    escape = [[False] * m for _ in range(n)]
    dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    ans = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                ans += 1

    return ans


n, m = list(map(int, input().split()))
graph = []
for _ in range(n):
    graph.append([d for d in input().rstrip()])
print(solution(n, m, graph))
