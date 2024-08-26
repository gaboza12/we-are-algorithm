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

from collections import deque, defaultdict


def solution(n, m, arr, start, end):
    # print(*arr, sep="\n")
    graph = defaultdict(list)
    for u, v in arr:
        graph[u].append(v)
        graph[v].append(u)
    for k, v in graph.items():
        v.sort()

    prev = [0] * (n+1)
    visited = [False] * (n+1)

    def bfs1(start, dest):
        prev[start] = start
        queue = deque()
        queue.append((0, start))
        while queue:
            print(queue)
            dist, curr = queue.popleft()
            if curr == dest:
                return dist

            for neighbor in graph[curr]:
                if prev[neighbor] != 0: continue
                prev[neighbor] = curr
                queue.append((dist+1, neighbor))

    def bfs2(start, end):
        queue = deque()
        queue.append((0, start))

        while queue:
            dist, curr = queue.popleft()
            if curr == end:
                return dist

            for neighbor in graph[curr]:
                if visited[neighbor]: continue
                visited[neighbor] = True
                queue.append((dist+1, neighbor))

    ans = bfs1(start, end)
    check = end
    while prev[check] != check:
        visited[check] = True
        check = prev[check]
    return ans + bfs2(end, start)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(m)]
    start, end = map(int, input().split())
    print(solution(n, m, arr, start, end))
