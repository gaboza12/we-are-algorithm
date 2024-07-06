# https://www.acmicpc.net/problem/14570

'''
1. 아이디어 :
    dfs를 통해서, 노드 자식이 2명일때, amount가 홀수면 왼쪽, 짝수면 오른쪽에 답이 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''
import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict

def solution(n, graph, k):
    ans = [0]

    def dfs(node, amount):
        if node not in graph:
            ans[0] = node
        elif len(graph[node]) == 1:
            dfs(graph[node][0], amount)
        elif len(graph[node]) == 2:
            if amount % 2 == 1:
                dfs(graph[node][0], (amount//2) + 1)
            else:
                dfs(graph[node][1], amount//2)

    dfs(1, k)
    return ans[0]


graph = defaultdict(list)
n = int(input())
for i in range(1, n + 1):
    arr = list(map(int, input().strip().split()))
    for child in arr:
        if child != -1:
            graph[i].append(child)
k = int(input())
print(solution(n, graph, k))
