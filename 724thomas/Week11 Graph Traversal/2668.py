# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque


def solution(n, arr):
    def bfs(num):
        visited = set()
        queue = deque()
        queue.append(num)
        visited.add(num)

        while queue:
            curr = queue.popleft()
            nxt = graph[curr]

            if nxt == num:
                return visited

            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
        return -1

    graph = defaultdict(int)
    for i in range(n):
        graph[i + 1] = arr[i]

    ans = set()
    for i in range(1, n+1):
        val = bfs(i)
        if val != -1:
            for n in val:
                ans.add(n)
    ans = sorted(list(ans))
    print(len(ans))
    for n in ans:
        print(n)


if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    solution(n, arr)
