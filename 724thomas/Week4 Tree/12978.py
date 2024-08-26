# https://www.acmicpc.net/problem/11978

'''
1. 아이디어 :
    dfs와 dp를 통해서 풀었습니다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열, 해시맵, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict

def solution(n, edges):
    dp = [[1, 0] for _ in range(n + 1)]  # [0] 경찰서가 있을때, [1] 없을때
    graph = defaultdict(list)
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node):
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            dfs(neighbor)

            dp[node][0] += min(dp[neighbor][0], dp[neighbor][1])
            dp[node][1] += dp[neighbor][0]
    visited.add(1)
    dfs(1)

    return min(dp[1])

n = int(input())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)]  # --> [ (a,b,..c) * n-1 ]
print(solution(n, edges))
