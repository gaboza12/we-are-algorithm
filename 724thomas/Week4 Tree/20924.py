# https://www.acmicpc.net/problem/20924

'''
1. 아이디어 :
    bfs로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    큐
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(n, root, edges):
    if n == 1:
        return (0, 0)
    dist = defaultdict(list)
    graph = defaultdict(list)
    for s, e, d in edges:
        graph[s].append(e)
        graph[e].append(s)
        dist[(s, e)] = d
        dist[(e, s)] = d

    to_giga = 0
    node = root

    queue = deque()
    queue.append((root, 0))
    visited = set()
    while len(queue) == 1:
        curr, dis = queue.popleft()
        visited.add(curr)
        nodes = graph[curr]
        for node in nodes:
            if node not in visited:
                queue.append((node, dis+dist[(curr, node)]))

    md = dis
    if not queue:
        return md, 0

    ed = 0
    while queue:
        curr, dis = queue.popleft()
        visited.add(curr)
        ed = max(ed, dis)
        nodes = graph[curr]
        for node in nodes:
            if node not in visited:
                queue.append((node, dis+ dist[(curr, node)]))


    return md, ed-md


n, root = list(map(int, input().split()))
edges = []
for _ in range(n - 1):
    edges.append(list(map(int, input().split())))
print(*solution(n, root, edges))
