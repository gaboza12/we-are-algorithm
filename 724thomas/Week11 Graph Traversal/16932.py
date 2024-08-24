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

from collections import deque, defaultdict

def solution(n, m, arr):

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    sectors = defaultdict(int)
    def bfs(row, col, sector):
        queue = deque()
        queue.append((row, col))
        size = 1

        while queue:
            x, y = queue.popleft()

            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] <= 0:
                    continue
                size += 1
                arr[nx][ny] = sector
                queue.append((nx,ny))
        return size

    def get_size(x, y):
        size = 1
        neighbors = set()
        for x2, y2 in dir:
            nx, ny = x+x2, y+y2
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            neighbors.add((arr[nx][ny]))
        for neighbor in neighbors:
            size += sectors[neighbor]
        return size

    ans = 0
    sector = -1
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 1:
                arr[row][col] = sector
                size = bfs(row,col, sector)
                ans = max(ans, size)
                sectors[sector] = size
                sector-=1
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 0:
                ans = max(ans, get_size(row, col))
    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))
