# https://www.acmicpc.net/problem/2533

'''
1. 아이디어 :
    dfs와 dp를 사용
    dp에 길이 2인 배열을 만든다. [인싸, 아싸]
    인싸는 친구(child)들이 인싸든 아싸든 최소값을 더하고, 아싸는 인싸 값을 더한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''

import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, edges):
    def dfs(node):
        include = 1
        exclude = 0
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            dfs(neighbor)
            include += min(dp[neighbor][0], dp[neighbor][1])
            exclude += dp[neighbor][0]
        dp[node] = [include, exclude]

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dp = defaultdict(list)

    root = 1
    visited = set([root])
    dfs(root)

    return min(dp[root][0], dp[root][1])

n = int(input().strip())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)]
print(solution(n, edges))