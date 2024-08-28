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
from itertools import combinations


def solution(n, m, arr):
    # print(*arr, sep="\n")
    graph = defaultdict(list)
    for u, v in arr:
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        dist = [-1] * (n + 1)
        dist[start] = 0
        queue = deque()
        queue.append(start)

        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if dist[neighbor] == -1:
                    dist[neighbor] = dist[curr] + 1
                    queue.append(neighbor)
        return dist

    all_distances = []
    for i in range(1, n + 1):
        all_distances.append(bfs(i))
    print(*all_distances, sep='\n')

    ans = float('inf')
    best = [0, 0]
    candid = [i for i in range(1, n + 1)]
    for comb in combinations(candid, 2):
        total = 0
        for i in range(1, n + 1):
            total += min(all_distances[i - 1][comb[0]], all_distances[i - 1][comb[1]])

        if total < ans:
            ans = total
            best = comb
    print(best[0], best[1], ans)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(m)]
    solution(n, m, arr)

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
