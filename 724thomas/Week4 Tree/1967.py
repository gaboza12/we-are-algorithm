# https://www.acmicpc.net/problem/1967

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, edges):
    ans = [0]
    graph = defaultdict(set)
    for u, v, d in edges:
        graph[u].add((v, d))

    def dfs(node):
        if node not in graph:
            return 0

        longest = 0
        longer = 0
        for neighbor, distance in graph[node]:
            neighbor_longer = distance + dfs(neighbor)
            if neighbor_longer > longest:
                longer = longest
                longest = neighbor_longer
            elif neighbor_longer > longer:
                longer = neighbor_longer
        ans[0] = max(ans[0], longest + longer)
        return longest

    visited = set()
    dfs(1)
    return ans[0]


n = int(input())
edges = []
for _ in range(n - 1):
    edges.append(list(map(int, input().split())))
print(solution(n, edges))
