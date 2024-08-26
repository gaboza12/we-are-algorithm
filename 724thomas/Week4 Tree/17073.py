# https://www.acmicpc.net/problem/17073

'''
1. 아이디어 :
    리프노드의 갯수 / 물
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    트리
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(n, m, edges):
    tree = defaultdict(list)

    for parent, child in edges:
        tree[parent].append(child)
        tree[child].append(parent)

    def dfs(node, parent):
        for child in tree[node]:
            if child == parent:
                continue
            if len(tree[child]) == 1:
                leaf_nodes.append(child)
            else:
                dfs(child, node)

    leaf_nodes = []
    dfs(1, -1)

    return m / len(leaf_nodes)


n, m = list(map(int, input().split()))
edges = []
for _ in range(n-1):
    parent, child = list(map(int, input().split()))
    if parent > child:
        parent, child = child, parent
    edges.append((parent, child))
print(solution(n, m, edges))


