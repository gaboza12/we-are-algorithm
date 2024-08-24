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
from collections import defaultdict

def solution(n, m, arr):
    # print(*arr, sep="\n")
    graph = defaultdict(list)
    for u, v in arr:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    def dfs(curr, depth):
        if depth == 4:
            print(1)
            exit()

        visited.add(curr)
        for neighbor in graph[curr]:
            if neighbor in visited: continue
            dfs(neighbor, depth+1)
        visited.remove(curr)

    for i in range(n):
        dfs(i, 0)
    return 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, arr))
