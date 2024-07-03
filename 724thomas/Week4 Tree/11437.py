# https://www.acmicpc.net/problem/11437

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, m, edges, pairs):
    def get_parents(node):
        parents = set([node])
        while par[node] in par:
            parents.add(par[node])
            node = par[node]
        return parents

    par = defaultdict(int)
    par[1] = -1
    for u, v in edges:
        if u > v:
            u, v = v, u
        par[v] = u

    for a, b in pairs:
        a_parents = get_parents(a)
        while True:
            if par[b] in a_parents:
                print(par[b])
                break
            else:
                b = par[b]
    return


n = int(input())
edges = [tuple(map(int, input().strip().split())) for _ in range(n - 1)]  # --> [ (a,b,..c) * n-1 ]
m = int(input())
pairs = [tuple(map(int, input().strip().split())) for _ in range(m)]  # --> [ (a,b,..c) * n-1 ]
print(solution(n, m, edges, pairs))
