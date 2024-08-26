# https://www.acmicpc.net/problem/16437

'''
1. 아이디어 :
    dfs로 풀 수 있다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, arr):
    graph = defaultdict(list)
    for i in range(len(arr)):
        u = i + 2
        v = arr[i+2][2]
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node):
        sheeps = 0
        wolves = 0
        if node in arr:
            if arr[node][0] == "W":
                wolves += arr[node][1]
            else:
                sheeps += arr[node][1]

        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            sheeps += dfs(child)


        return max(0, sheeps -wolves)

    visited = set()
    visited.add(1)
    return dfs(1)


n = int(input())
arr = {}
for i in range(n - 1):
    a, b, c = input().split()
    arr[i+2] = (a, int(b), int(c))
print(solution(n, arr))
