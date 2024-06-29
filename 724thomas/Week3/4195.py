# https://www.acmicpc.net/problem/4195

'''
1. 아이디어 :
    union-find
    사이즈를 트래킹하면서 풀었습니다.
    a - b, b -c, c - a 케이스도 확인
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, edges):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(f1, f2):
        f1 = find(f1)
        f2 = find(f2)

        if f1 != f2:
            if size[f1] > size[f2]:
                par[f2] = f1
                size[f1] += size[f2]
            else:
                par[f1] = f2
                size[f2] += size[f1]
                if size[f1] == size[f2]:
                    size[f2] += 1

    idx_name = defaultdict(str)
    name_idx = defaultdict(int)

    cmax = 0
    par = []
    size = []

    for f1, f2 in edges:
        if f1 not in name_idx:
            idx_name[cmax] = f1
            name_idx[f1] = cmax
            par.append(cmax)
            size.append(1)
            cmax += 1
        if f2 not in name_idx:
            idx_name[cmax] = f2
            name_idx[f2] = cmax
            par.append(cmax)
            size.append(1)
            cmax += 1

        if find(name_idx[f1]) == find(name_idx[f2]):
            print(size[find(name_idx[f1])])
        else:
            print(size[find(name_idx[f1])] + size[find(name_idx[f2])])
        union(name_idx[f1], name_idx[f2])


for _ in range(int(input())):
    n = int(input())
    edges = []
    for _ in range(n):
        edges.append(list(map(str, input().split())))
    solution(n, edges)
