# https://www.acmicpc.net/problem/19581

'''
1. 아이디어 :
    bfs를 4번 돌려야한다.
    가장 먼 노드들 A, B를 찾는다.
    A에서 B를 방문하지 않고 가장 먼 노드의 거리와
    B에서 A를 방문하지 않고 가장 먼 노드의 거리 중 큰걸 리턴한다.
    (visited에서 A와 B를 추가하고 시작하면된다)
    간당간당하게 시간초과가 안난다. (같은 답이라도 가끔 시간초과)
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋. 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(n, graph):
    def bfs(node):
        queue = deque()
        queue.append((node, 0))
        far_node = node
        far_dist = 0

        while queue:
            curr, total = queue.popleft()
            if far_dist < total:
                far_dist = total
                far_node = curr

            for neighbor, distance in graph[curr]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append((neighbor, total + distance))

        return far_node, far_dist

    visited = set()
    visited.add(1)
    far_nodeA, _ = bfs(1)

    visited.clear()
    visited.add(far_nodeA)
    far_nodeB, _ = bfs(far_nodeA)

    visited.clear()
    visited.add(far_nodeA)
    visited.add(far_nodeB)
    _, far_distanceA = bfs(far_nodeB)

    visited.clear()
    visited.add(far_nodeA)
    visited.add(far_nodeB)
    _, far_distanceB = bfs(far_nodeA)

    return max(far_distanceA, far_distanceB)


n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v, d = list(map(int, input().strip().split()))
    graph[u].append((v, d))
    graph[v].append((u, d))
print(solution(n, graph))
