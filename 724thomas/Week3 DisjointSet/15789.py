# https://www.acmicpc.net/problem/15789

'''
1. 아이디어 :
    union-find
    왕국들을 연결시킨다.
    각 왕국들의 사이즈별로 정렬
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, edges, c, h, k):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra != rb:
            if size[ra] < size[rb]:
                par[rb] = ra
                size[ra] += size[rb]
            else:
                par[ra] = rb
                size[rb] += size[ra]

    par = [i for i in range(n + 1)]
    size = [1 for i in range(n + 1)]
    candid = set()
    for u, v in edges:
        union(u, v)
    c = find(c)
    h = find(h)
    for i in range(1, len(par)):
        ra = find(par[i])
        if ra == c or ra == h:
            continue
        candid.add((size[ra], ra))

    candid = sorted(list(candid), reverse=True)
    ans = size[find(c)]
    for i in range(k):
        ans += candid[i][0]
    return ans


n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
c, h, k = list(map(int, input().split()))
print(solution(n, m, edges, c, h, k))
