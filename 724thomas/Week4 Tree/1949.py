# https://www.acmicpc.net/problem/1949

'''
1. 아이디어 :
    dp와 dfs로 풀 수 있다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵, 해시셋, 배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict, deque
def solution(n, pop, graph):
    def dfs(node):
        dp[node][0] = pop[node]

        for neighbor in graph[node]:
            if neighbor in visited:
                continue
            visited.add(neighbor)
            dfs(neighbor)
            dp[node][0] += dp[neighbor][1]# 우수일때
            dp[node][1] += max(dp[neighbor][0], dp[neighbor][1]) #비우수일때


    dp = [[0,0] for _ in range(n+1)] # 우수, 비우수
    visited = set()
    visited.add(1)
    dfs(1)
    return max(dp[1])

n = int(input())
pop = [0] + list(map(int, input().strip().split()))
graph = defaultdict(list)
for _ in range(n-1):
    u, v = list(map(int, input().strip().split()))
    graph[u].append(v)
    graph[v].append(u)
print(solution(n, pop, graph))


