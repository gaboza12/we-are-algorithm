# https://www.acmicpc.net/problem/19535

'''
1. 아이디어 :
    점화식이 어려웠다.
    g는 p * (p-1) * (p-2) / 6
    d는 (len(graph[node]) -1) * (len(graph[neighbor]) -1)
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시셋
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, depth):
        if len(graph[node]) >= 3:
            points = len(graph[node])
            g[0] += points * (points-1) * (points-2) / 6

        for neighbor in graph[node]:
            if neighbor in visited: continue
            visited.add(neighbor)
            dfs(neighbor, depth+1)
            if len(graph[node]) >= 2 and len(graph[neighbor]) >= 2:
                d[0] += (len(graph[node]) -1) * (len(graph[neighbor]) -1)

    g = [0]
    d = [0]
    visited = set()
    visited.add(1)
    dfs(1, 0)

    if d[0] == g[0] * 3:
        print("DUDUDUNGA")
    elif d[0] > g[0] * 3:
        print("D")
    else:
        print("G")

    return


n = int(input())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)] # --> [ (a,b,..c) * n-1 ]
solution(n, edges)


