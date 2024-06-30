# https://www.acmicpc.net/problem/11085

'''
1. 아이디어 :
    kruskal 알고리즘을 사용.
    width, a, b를 width 기준으로 정렬한다.
    width가 큰 a-b부터 연결시키고, c와 v가 연결됬는지 확인.
    연결 되어 있으면 width가 정답
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque


def solution(p, w, c, v, edges):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[ra] < rank[rb]:
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1

    par = [i for i in range(p)]
    rank = [1 for _ in range(p)]

    edges.sort(reverse=True, key=lambda x: x[0])

    max_bandwidth = float('inf')
    for weight, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            max_bandwidth = min(max_bandwidth, weight)
            if find(c) == find(v):
                return max_bandwidth


p, w = list(map(int, input().split()))
c, v = list(map(int, input().split()))
edges = []
for _ in range(w):
    a, b, d = list(map(int, input().split()))
    edges.append((d, a, b))
print(solution(p, w, c, v, edges))
