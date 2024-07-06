# https://www.acmicpc.net/problem/20040

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


def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

def union(a, b):
    ra = find(a)
    rb = find(b)

    if rank[ra] > rank[rb]:
        par[rb] = ra
    elif rank[rb] < rank[ra]:
        par[ra] = rb
    else:
        par[rb] = ra
        rank[ra] += 1

n, m = list(map(int, input().split()))
par = [i for i in range(n)]
rank = [1 for i in range(n)]
edges = []
for i in range(m):
    u, v = list(map(int, input().split()))
    if find(u) == find(v):
        print(i+1)
        exit()
    union(u, v)
print(0)


