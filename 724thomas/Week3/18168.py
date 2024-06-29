# https://www.acmicpc.net/problem/18168

'''
1. 아이디어 :
    모든 길을 방문하는 조건 (오일러 법칙)
    1. 정점의 길이 홀수인 정점의 수가 0 또는 2여야 한다.
    2. 모든 정점이 연결되있어야 한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(places, roads, edges):
    def bfs(node):
        visited = set()
        visited.add(node)
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        return len(visited) == places

    graph = defaultdict(set)
    degree = [0] * (roads + 1)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
        degree[u] += 1
        degree[v] += 1

    count_odds = 0
    for n in degree:
        if n % 2 == 1:
            count_odds += 1
            if count_odds > 2:
                return "NO"
    if count_odds == 1:
        return "NO"

    return "YES" if bfs(1) else "NO"


v, e = list(map(int, input().split()))
edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))
print(solution(v, e, edges))

'''
1    
  3  2
4

1 - 2     
1 - 3
1 - 4
2 - 3
2 - 4

'''
