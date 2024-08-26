# https://www.acmicpc.net/problem/19641

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    해시맵, 해시셋
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, edges, root):
    visited = set()
    curr = [0]
    ans = {}
    def dfs(node):
        curr[0] += 1
        temp = curr[0]
        for child in edges[node]:
            if child not in visited:
                visited.add(child)
                dfs(child)

        curr[0] += 1
        ans[node] = (temp, curr[0])



    visited.add(root)
    dfs(root)
    for i in range(1, n+1):
        print(i, *ans[i])


n = int(input())
edges = defaultdict(list)
for _ in range(n):
    temp = list(map(int, input().strip().split()))
    edges[temp[0]] = sorted(temp[1:len(temp) - 1])
root = int(input())
solution(n, edges, root)
