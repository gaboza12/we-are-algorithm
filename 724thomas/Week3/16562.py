# https://www.acmicpc.net/problem/16562

'''
1. 아이디어 :
    union-find를 사용해서 연결하고,
    각 친구의 부모의 최소값을 구한다.
2. 시간복잡도 :
    O( n*e )
3. 자료구조 :
    배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import defaultdict
def solution(n, m, k, edges):

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

    for u, v in edges:
        union(u, v)

    min_price = defaultdict(int)
    for friend in range(n):
        par = find(friend)
        if par not in min_price:
            min_price[par] = prices[friend]
        else:
            min_price[par] = min(min_price[par], prices[friend])

    total = sum(min_price.values())
    return "Oh no" if total > k else total


n, m, k = list(map(int, input().split()))
prices = list(map(int, input().split()))
edges = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    edges.append((a-1, b-1))
print(solution(n, m, k, edges))


