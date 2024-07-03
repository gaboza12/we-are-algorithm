# https://www.acmicpc.net/problem/12912

'''
1. 아이디어 :
    간선을 하나씩 지웠다가 추가한다.
    간선이 하나씩 지워지면 트리가 2개가 생기는데, 각 트리의 가장 긴 지름 + 지워진 간선의 길이가 최대 값이 되게 한다.
2. 시간복잡도 :
    O( e * 4n )
3. 자료구조 :
    배열, 해시맵, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(n, edges, graph):

    def bfs(node):
        visited = set()
        visited.add(node)
        queue = deque()
        queue.append((node, 0)) #node, distance
        farthest_node = node
        farthest_distance = 0
        while queue:
            curr, total = queue.popleft()
            if farthest_distance < total:
                farthest_distance = total
                farthest_node = curr

            for neighbor, distance in graph[curr]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append((neighbor, total + distance))
        return farthest_node, farthest_distance

    def get_diameter(node1, node2):
        farthest_node1, _ = bfs(node1)
        _, farthest_distance1 = bfs(farthest_node1)
        farthest_node2, _ = bfs(node2)
        _, farthest_distance2 = bfs(farthest_node2)
        return farthest_distance1 + farthest_distance2

    ans = 0
    for u, v, d in edges:
        graph[u].remove((v,d))
        graph[v].remove((u,d))
        ans = max(ans, get_diameter(u, v) + d)
        graph[u].add((v,d))
        graph[v].add((u,d))
    return ans

n = int(input())
graph = defaultdict(set)
edges = []
for _ in range(n - 1):
    u, v, d = list(map(int, input().strip().split()))
    edges.append((u,v,d))
    graph[v].add((u, d))
    graph[u].add((v, d))
print(solution(n, edges, graph))
