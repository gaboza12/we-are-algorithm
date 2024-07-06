# https://www.acmicpc.net/problem/18116

'''
1. 아이디어 :
    union-find
    union을 다 하고 출력하는게 아니라 도중에 출력한다. 거지같은 문제
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열, 해시맵
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(n, commands):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA != rootB:
            if rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
                size[rootA] += size[rootB]
            else:
                parent[rootA] = rootB
                size[rootB] += size[rootA]
                if rank[rootA] == rank[rootB]:
                    rank[rootB] += 1

    max_size = 1000001
    parent = list(range(max_size))
    size = [1] * max_size
    rank = [1] * max_size

    ans = []

    for command in commands:
        if command[0] == "I":
            u, v = int(command[1]), int(command[2])
            union(u, v)
        else:
            q = find(int(command[1]))
            ans.append(size[q])

    for a in ans:
        print(a)

n = int(input())
commands = [input().strip().split() for _ in range(n)]
solution(n, commands)
