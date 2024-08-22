# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr):
    graph = [x - 1 for x in arr]  # 0-indexed로 변환
    visited = [False] * n
    finished = [False] * n  # DFS가 끝난 노드를 추적
    result = 0

    def dfs(node):
        nonlocal result
        visited[node] = True
        next_node = graph[node]

        if not visited[next_node]:
            if dfs(next_node):
                finished[node] = True
                return True
        elif not finished[next_node]:
            # 사이클이 발견된 경우
            temp = next_node
            cycle_length = 0
            while temp != node:
                cycle_length += 1
                temp = graph[temp]
            cycle_length += 1
            result += cycle_length

        finished[node] = True
        return False

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return n - result

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(solution(n, arr))
