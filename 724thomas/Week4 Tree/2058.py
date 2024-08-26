# https://www.acmicpc.net/problem/2058

'''
1. 아이디어 :
    노드의 간선들을 구한다.
    길이가 2인 dp 배열을 만들고, bottom-up으로 실행.
    dp배열의 0번째는 해당 노드를 포함하지 않았을때의 최대, 1번째는 포함했을때의 최대
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, m, nodes, diffs):
    def dfs(node):
        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            dfs(neighbor)

            dp[node][0] += max(dp[neighbor][0], dp[neighbor][1]) # 현재 노드를 포함하지 않았을때 최대
            dp[node][1] += dp[neighbor][0] #현재 노드를 포함할때 최대

    nodes_set = set(nodes)
    graph = defaultdict(list)

    for diff in diffs: # 간선 구하기
        for node in nodes_set:
            if node-diff in nodes_set:
                graph[node].append(node-diff)
            if node+diff in nodes_set:
                graph[node].append(node+diff)

    dp = defaultdict(list)
    for node in nodes_set:
        dp[node] = [0, node]

    start_node = min(nodes)
    visited = set([start_node])

    dfs(start_node)
    return max( dp[start_node][0], dp[start_node][1])


n, m = list(map(int, input().split()))
nodes = []
for _ in range(n):
    nodes.append(int(input()))
diff = []
for _ in range(m):
    diff.append(int(input()))
print(solution(n, m, nodes, diff))
