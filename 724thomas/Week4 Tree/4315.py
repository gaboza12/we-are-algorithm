# https://www.acmicpc.net/problem/4315

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(n, marbles, edges):
    graph = defaultdict(list)
    marbles = {arr[0] : arr[1] for arr in marbles}
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        visited.add(v)
    ans = [0]

    def find_root():
        for i in range(1, n + 1):
            if i not in visited:
                return i

    def dfs(node):
        temp = 0
        for child in graph[node]:
            temp += dfs(child)
        total = temp + marbles[node] - 1
        ans[0] += abs(total)
        return total

    root = find_root()
    dfs(root)
    return ans[0]


while True:
    n = int(input())
    if n == 0:
        exit()
    edges = []
    marbles = []
    for _ in range(n):
        arr = list(map(int, input().strip().split()))
        node = arr[0]
        marble = arr[1]
        marbles.append((node, marble))
        children = arr[2]
        for i in range(3, len(arr)):
            edges.append((node, arr[i]))
    print(solution(n, marbles, edges))
