# https://www.acmicpc.net/problem/1976

'''
1. 아이디어 :
    union-find
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, edges, path):

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            if rank[a] > rank[b]:
                par[b] = a
            elif rank[a] < rank[b]:
                par[a] = b
            else:
                par[a] = b
                rank[b] += 1

    par = [i for i in range(n)]
    rank = [1 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if edges[i][j] == 1:
                union(i, j)

    for i in range(1, len(path)):
        if find(path[i-1]-1) != find(path[i]-1):
            return "NO"
    return "YES"


n = int(input())
m = int(input())
edges = []
for _ in range(n):
    edges.append(list(map(int, input().split())))
path = list(map(int, input().split()))
print(solution(n, m, edges, path))
