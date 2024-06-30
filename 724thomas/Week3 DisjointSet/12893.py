# https://www.acmicpc.net/problem/12893

'''
1. 아이디어 :
    배열길이 2n + 1개를 초기화한다.
    n+1까지는 노드, 나머지 2n+1까지는 노드의 적으로 간주한다.
    예를 들어 n=5이고,
    1 2가 들어오면, 1의 적인 6은 2의 친구다. 반대로 2의 적인 7은 1의 친구다.
    union(2,6), union(1,7)을 하게 된다.
    그 뒤에 2, 3를 하게 되면
    union(2, 8), union(3, 7). ->
    [0, 1, 2, 1, 4, 5, 2, 1, 2, 9, 10]
    이제 1 3을 하게 됬을떄 find(1,3)은 같은 그룹에 있으므로 성립되지 않는다.
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
    if ra != rb:
        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[ra] < rank[rb]:
            rank[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1


n, m = list(map(int, input().split()))
par = [i for i in range(2 * n + 1)]
rank = [1 for i in range(2 * n + 1)]

for i in range(m):
    u, v = list(map(int, input().split()))
    ru, rv = find(u), find(v)

    if ru == rv:
        print(0)
        exit()
    union(u, v + n)
    union(v, u + n)

print(1)
