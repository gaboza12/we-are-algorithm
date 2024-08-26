# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(N, R, Q, edges):
    graph = defaultdict(list)
    scores = defaultdict(list)
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node):
        visited.add(node)

        points = 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                points += dfs(neighbor)

        scores[node] = points
        return points

    dfs(R)
    for _ in range(Q):
        print(scores[int(input())])


N, R, Q = list(map(int, input().split()))
edges = []
for _ in range(N - 1):
    edges.append(list(map(int, input().split())))
solution(N, R, Q, edges)
