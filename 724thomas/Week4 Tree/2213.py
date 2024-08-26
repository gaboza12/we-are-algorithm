# https://www.acmicpc.net/problem/2213

'''
1. 아이디어 :
    dp를 사용해서 최대 값을 구하고
    최대값을 타고가면서 노드들을 구한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, score, graph):
    def dfs(node):
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            dfs(child)

            dp[node][0] += dp[child][1]      #포함
            dp[node][1] += max(dp[child][0], dp[child][1])     #미포함

    def get_path(node, included):
        if included:
            path.append(node)
        for child in graph[node]:
            if child in visited:
                continue
            visited.add(child)
            if included:
                get_path(child, False)
            else:
                if dp[child][0] > dp[child][1]:
                    get_path(child, True)
                else:
                    get_path(child, False)

    dp = [[score[i], 0] for i in range(n+1)]
    visited = set()
    visited.add(1)
    dfs(1)

    visited = set()
    visited.add(1)
    path = []
    if dp[1][0] > dp[1][1]:
        get_path(1, True)
    else:
        get_path(1, False)

    print(max(dp[1]))
    print(*sorted(path))
    return


n = int(input())
score = [0] + list(map(int, input().strip().split()))
graph = defaultdict(list)
for _ in range(n-1):
    u, v = list(map(int, input().strip().split()))
    graph[u].append(v)
    graph[v].append(u)
solution(n, score, graph)
