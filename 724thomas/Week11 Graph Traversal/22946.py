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
import math

def solution(n, arr):
    # print(arr)
    arr.append((0,0,float('inf')))
    arr.sort(key=lambda x: -x[2])

    def calc_distance(x1, y1, x2, y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def make_tree():
        graph = defaultdict(list)
        depth = [0] * n
        pars = defaultdict(set)
        for i in range(n):
            x, y, r = arr[i]
            for j in range(i+1, n):
                if i == j: continue
                x2, y2, r2 = arr[j]
                if calc_distance(x, y, x2, y2) < r and r>r2:
                    pars[j].add(i)
                    depth[j] += 1

        for child, par_set in pars.items():
            child_depth = depth[child]
            for par in par_set:
                par_depth = depth[par]
                if child_depth - par_depth == 1:
                    graph[par].append(child)
                    graph[child].append(par)
        return graph

    def bfs(i):
        visited = set()
        visited.add(i)
        queue = deque()
        queue.append((i, 0)) #curr, distance

        farthest_d = -1
        farthest_n = -1
        while queue:
            curr, distance = queue.popleft()
            if distance > farthest_d:
                farthest_d = distance
                farthest_n = curr

            for neighbor in graph[curr]:
                if neighbor in visited: continue
                visited.add(neighbor)
                queue.append((neighbor, distance+1))

        return farthest_n, farthest_d

    graph = make_tree()
    farthest_n, _ = bfs(0)
    _, farthest_d = bfs(farthest_n)
    return farthest_d


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))
