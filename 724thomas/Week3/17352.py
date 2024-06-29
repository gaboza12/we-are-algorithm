# https://www.acmicpc.net/problem/17352

'''
1. 아이디어 :
    union-find
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열, 해시셋
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, edges):

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a,b):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB:
            if rootA < rootB:
                par[rootB] = rootA
            else:
                par[rootA] = rootB

    par = [i for i in range(n+1)]
    for u, v in edges:
        union(u, v)
    ans = set()
    for i in range(1, n+1):
        ans.add(find(i))
    return list(ans)

n = int(input())
edges = []
for i in range(n-2):
    edges.append(list(map(int, input().split())))
print(*solution(n, edges))


