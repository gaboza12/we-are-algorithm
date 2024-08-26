# https://www.acmicpc.net/problem/19542

'''
1. 아이디어 :
    리프노드부터 root까지 거리를 구하고, 거리가 d이상인 노드들의 합 x 2
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque
def solution(n, root, edges, d):

    def dfs(node, parent):
        max_dist = 0
        for child in graph[node]:
            if child != parent:
                child_dist = dfs(child, node) + 1
                max_dist = max(max_dist, child_dist)
        distance[node] = max_dist
        return max_dist

    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    distance = [0] * (n+1)
    dfs(root, -1)

    ans = 0
    for i in range(1, n+1):
        if distance[i] >= d:
            ans += 1
    return max(0, (ans-1) * 2)


n, root, d = list(map(int, input().strip().split()))
edges = []
for _ in range(n-1):
    a, b = list(map(int, input().strip().split()))
    if a > b:
        a, b = b, a
    edges.append((a, b))
print(solution(n, root, edges, d))
