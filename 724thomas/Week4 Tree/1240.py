# https://www.acmicpc.net/problem/1240

'''
1. 아이디어 :
    dfs로 풀수 있다
2. 시간복잡도 :
    O( n^3 )
3. 자료구조 :
    해시맵, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import deque, defaultdict


def solution(n, m, edges, between):
    graph = defaultdict(list)
    dist = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for u, v, d in edges:
        graph[u].append(v)
        graph[v].append(u)
        dist[u][v] = d
        dist[v][u] = d

    def bfs(start):
        visited = set()
        queue = deque()
        queue.append((start, 0))
        visited.add(start)
        while queue:
            node, total = queue.popleft()
            dist[start][node] = total
            dist[node][start] = total
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, total + dist[node][child]))
    for i in range(1, n+1):
        bfs(i)

    for u, v in between:
        print(dist[u][v])



n, m = list(map(int, input().split()))
edges = []
between = []
for _ in range(n - 1):
    edges.append(list(map(int, input().split())))
for _ in range(m):
    between.append(list(map(int, input().split())))
solution(n, m, edges, between)
