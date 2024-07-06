# https://www.acmicpc.net/problem/1595

'''
1. 아이디어 :
    임의의 정점에서 bfs를 돌려서 가장 먼 곳의 정점을 찾고, 해당 정점에서 다시한번 bfs
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(graph):
    def bfs(start):
        visited = set()
        visited.add(start)
        queue = deque()
        queue.append((start, 0))
        furthest = start
        furthest_d = 0
        while queue:
            node, total = queue.popleft()

            if total > furthest_d:
                furthest_d = total
                furthest = node

            for child, distance in graph[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append((child, total + distance))

        return furthest, furthest_d

    furthest, furthest_d = bfs(1)
    return max(furthest_d, bfs(furthest)[1])


graph = defaultdict(list)
edges = []
while True:
    try:
        u, v, d = list(map(int, input().strip().split()))
        graph[u].append((v, d))
        graph[v].append((u, d))
    except:
        break
print(solution(graph))
