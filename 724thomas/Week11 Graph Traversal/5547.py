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

from collections import deque


def solution(m, n, arr):
    even_dir = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [0, 1]]
    odd_dir = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [0, -1]]

    narr = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            narr[i + 1][j + 1] = arr[i][j]

    ans = 0
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * (m + 2) for _ in range(n + 2)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        directions = even_dir if x % 2 == 0 else odd_dir
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(narr) and 0 <= ny < len(narr[0]):
                if narr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif narr[nx][ny] == 1:
                    ans += 1
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, arr))
