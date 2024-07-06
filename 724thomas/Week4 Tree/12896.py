# https://www.acmicpc.net/problem/12896

'''
1. 아이디어 :
    2번의 bfs로 임의의 도시에서 가장 먼 도시를 구하고, 그 도시에서 가장 먼 도시를 구한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque
import math
def solution(n, edges):
    graph = defaultdict(list)
    visited = set()

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    def bfs(node):
        cmax = 0
        city = 0
        visited=set()
        visited.add(node)
        queue = deque()
        queue.append((node,0))

        while queue:
            node, distance = queue.popleft()
            visited.add(node)
            if distance > cmax:
                city = node
                cmax = distance

            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                queue.append((neighbor, distance+1))

        return city, cmax

    city, distance = bfs(1)
    return math.ceil(bfs(city)[1]/2)

n = int(input())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)] # --> [ (a,b,..c) * n-1 ]
print(solution(n, edges))


