# https://www.acmicpc.net/problem/17398

'''
1. 아이디어 :
    쿼리에 q번째 간선을 제거하는 순서를 반대로 연결한다.
    1-2, 2-3, 3-4, 1-4 이고, q가 4, 2, 3일때,
    1-2를 먼저 연결하고, 3(3-4), 2(2-3), 4(1-4)를 연결한다.
    연결하기 전에, 두 탑의 사이즈를 곱해서 ans를 갱신한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, q, edges, disconnect):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return
        if size[ra] >= size[rb]:
            par[rb] = ra
            size[ra] += size[rb]
        else:
            par[ra] = rb
            size[rb] += size[ra]

    par = [i for i in range(n + 1)]
    size = [1 for _ in range(n + 1)]

    disconnect.reverse()
    initial = [True] * m
    for d in disconnect:
        initial[d - 1] = False

    for i, edge in enumerate(edges):
        if initial[i]:
            union(*edge)
    ans = 0
    for d in disconnect:
        u, v = edges[d - 1]
        u = find(u)
        v = find(v)
        if u == v:
            continue
        ans += size[u] * size[v]
        union(u, v)

    return ans


n, m, q = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
disconnect = []
for _ in range(q):
    disconnect.append(int(input()))

print(solution(n, m, q, edges, disconnect))
