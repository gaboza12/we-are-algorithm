# https://www.acmicpc.net/problem/4803

'''
1. 아이디어 :
    트리를 확인하면서 순회
2. 시간복잡도 :
    O( n (
3. 자료구조 :
    해시맵, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(idx, n, m, edges):

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n+1)

    ans = [n]

    def is_tree(node, parent):
        visited[node] = True
        for child in graph[node]:
            if not visited[child]:
                if not is_tree(child, node):
                    return False
            elif child != parent:
                return False
        return True

    tree_count = 0
    for i in range(1, n + 1):
        if not visited[i]:
            if is_tree(i, -1):
                tree_count += 1

    s = f"Case {idx}: "
    if tree_count == 0:
        return s + "No trees."
    elif tree_count == 1:
        return s + "There is one tree."
    else:
        return s + f"A forest of {tree_count} trees."



idx = 1
while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        exit()
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(solution(idx, n, m, edges))
    idx += 1
