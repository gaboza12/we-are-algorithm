# https://www.acmicpc.net/problem/7511

'''
1. 아이디어 :
    union - find
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, k, m, edges, query):

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a,b):
        ra = find(a)
        rb = find(b)

        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[rb] < rank[ra]:
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1


    par = [i for i in range(n+1)]
    rank = [1 for i in range(n+1)]
    for u, v in edges:
        union(u,v)
    for u, v in query:
        if find(u) == find(v):
            print(1)
        else:
            print(0)


for i in range(int(input())):
    n = int(input())
    k = int(input())
    edges = []
    for _ in range(k):
        edges.append(list(map(int, input().strip().split())))

    m = int(input())
    query = []
    for _ in range(m):
        query.append(list(map(int, input().strip().split())))
    print("Scenario " + str(i+1) + ":")
    solution(n, k, m, edges, query)
    print()
