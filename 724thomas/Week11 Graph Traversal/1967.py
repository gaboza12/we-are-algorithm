# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque


def solution(n, arr):
    def get_furthest(curr):
        visited = set()
        visited.add(curr)
        queue = deque()
        queue.append((curr, 0))
        furthest_distance = 0
        furthest_node = curr
        while queue:
            curr, dist = queue.popleft()
            if dist > furthest_distance:
                furthest_node = curr
                furthest_distance = dist

            for next_node, distance in graph[curr]:
                if next_node in visited:
                    continue
                visited.add(next_node)
                queue.append((next_node, dist + distance))

        return furthest_node, furthest_distance

    # print(*arr, sep="\n")
    graph = defaultdict(list)
    for u, v, d in arr:
        graph[u].append((v,d))
        graph[v].append((u,d))

    start_node, _ = get_furthest(1)
    _, distance = get_furthest(start_node)

    return distance


if __name__ == '__main__':
    n = int(input())
    # n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n - 1)]
    print(solution(n, arr))
