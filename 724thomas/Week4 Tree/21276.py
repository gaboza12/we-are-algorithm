# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    최고 조상을 찾으면서, 부모의 수만큼 몇번째 자식인지 찾는다.
    사람마다 사람의 자식이 본인의 레벨(부모 수) + 1이면, 바로 아래 자식이다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    해시맵, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import defaultdict


def solution(p, people, n, childs, parents):
    people.sort()
    roots = []
    levels = {}
    for p in people:
        if p not in pars:
            roots.append(p)
        if p not in parents:
            levels[p] = 0
        else:
            levels[p] = len(parents[p])

    edges = defaultdict(list)
    for parent in people:
        for child in childs[parent]:
            if levels[parent] == levels[child] - 1:
                edges[parent].append(child)

    print(len(roots))
    print(*sorted(roots))
    for p in people:
        print(p, len(edges[p]), *sorted(edges[p]))


p = int(input())
people = list(map(str, input().split()))
n = int(input())
childs = defaultdict(set)
pars = defaultdict(set)
for _ in range(n):
    child, par = list(map(str, input().split()))
    childs[par].add(child)
    pars[child].add(par)
solution(p, people, n, childs, pars)
