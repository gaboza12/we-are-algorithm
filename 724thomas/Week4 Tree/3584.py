# https://www.acmicpc.net/problem/3584

'''
1. 아이디어 :
    dfs로 풀려다가 실패.
    단순히 a의 부모들의 집합을 만들어놓고, b가 존재하는지 확인.
    존재하지 않으면 b는 b의 부모로 갱신한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(n, edges, target):
    parent = defaultdict(int)
    for u, v in edges:
        parent[v] = u

    def find_ancesters(node):
        ancesters = set()
        while node in parent:
            ancesters.add(node)
            node = parent[node]
        ancesters.add(node)
        return ancesters

    a, b = target
    ancesters_a = find_ancesters(a)
    while b not in ancesters_a:
        b = parent[b]

    return b


for _ in range(int(input())):
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    target = list(map(int, input().split()))
    print(solution(n, edges, target))




