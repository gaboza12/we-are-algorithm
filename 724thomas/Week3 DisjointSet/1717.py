# https://www.acmicpc.net/problem/1717

'''
1. 아이디어 :
    Union-find 사용
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, commands):
    par = [i for i in range(n + 1)]
    rank = [0] * (n + 1)

    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB:
            if rank[rootA] > rank[rootB]:
                par[rootB] = rootA
            else:
                par[rootA] = rootB
                if rank[rootA] == rank[rootB]:
                    rank[rootB] += 1

    def find(x):
        while par[x] != x:
            x = par[x]
        return x

    for c, a, b in commands:
        if c == 0:
            union(a, b)
        elif c == 1:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")


n, m = list(map(int, input().split()))
commands = []
for _ in range(m):
    commands.append(list(map(int, input().split())))
solution(n, m, commands)
