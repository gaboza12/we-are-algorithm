# https://www.acmicpc.net/problem/14657

'''
1. 아이디어 :
    가장 멀리 있는 문제를 bfs로 구한다.
    가장 멀리 있는 문제에서 다른 가장 멀리있는 문제를 bfs로 다시 한번 구한다.
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
def solution(n, m, edges):

    def bfs(curr):
        visited = set()
        visited.add(curr)
        queue = deque()
        queue.append((curr, 0, 0))  # node, distance, max_count

        farthest_node = curr
        max_distance = 0
        max_count = 0

        while queue:
            node, distance, count = queue.popleft()
            if max_count < count:
                farthest_node = node
                max_distance = distance
                max_count = count
            if max_count == count and max_distance > distance:
                farthest_node = node
                max_distance = distance

            for neighbor, time in edges[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append( (neighbor, distance + time, count+1) )

        return farthest_node, max_distance, max_count

    farthest_node, _, _ = bfs(1)
    farthest_node, distance, _ = bfs(farthest_node)
    return math.ceil(distance/m)

n, m = list(map(int, input().strip().split()))
edges = defaultdict(list)
for _ in range(n-1):
    par, child, time = list(map(int, input().strip().split()))
    edges[par].append((child, time))
    edges[child].append((par, time))
print(solution(n, m, edges))


