# https://www.acmicpc.net/problem/20955

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


def solution(n, m, edges):
    def find(x):
        while par[x] != x:
            x = par[x]
        return x

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True

    par = [i for i in range(n + 1)]
    rank = [1] * (n + 1)
    provinces = n
    no_need = 0

    for u, v in edges:
        if union(u, v):
            no_need += 1
        else:
            provinces += 1

    return provinces - 1 - no_need


n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
print(solution(n, m, edges))
