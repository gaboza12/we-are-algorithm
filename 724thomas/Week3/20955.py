# https://www.acmicpc.net/problem/20955

'''
1. 아이디어 :
    union - find
    연결해야될 정점의 갯수 n에서 연결할때마다, 갯수를 1개씩 줄여준다.
    이미 연결되어 있을때 또 연결하면 트리가 안되므로 해당 연결점은 필요가 없다.
    마지막으로 정점의 갯수 만큼 서로 연결하려면 갯수-1만큼의 연결선이 필요하기때문에 province - 1 + delete가 답
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(v, e, edges):

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a,b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return True

        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[ra] < rank[rb]:
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1


    par = [i for i in range(v+1)]
    rank = [1 for _ in range(v+1)]

    province = v
    delete = 0

    for u, v in edges:
        if union(u, v):
            delete += 1
        else:
            province -= 1

    return province - 1 + delete #province를 서로 연결하기 위해서는 필요한 간선은 province - 1


v, e = list(map(int, input().split()))
edges = []
for _ in range(e):
    edges.append(list(map(int, input().split())))

print(solution(v, e, edges))


