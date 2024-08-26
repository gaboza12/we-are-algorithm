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


def solution(m, n, k, arr):
    print(*arr, sep='\n')
    queue = deque()
    for height in range(k):
        for row in range(n):
            for col in range(m):
                if arr[height][row][col] == 1:
                    queue.append((height, row, col))

    dir = [[0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0], [0, 0, 1], [0, 0, -1]]

    while queue:
        x, y, z = queue.popleft()
        next_val = arr[x][y][z] + 1

        for x2, y2, z2 in dir:
            nx, ny, nz = x + x2, y + y2, z + z2
            if not (0 <= nx < k and 0 <= ny < n and 0<= nz < m) or arr[nx][ny][nz] != 0:
                continue
            arr[nx][ny][nz] = next_val
            queue.append((nx, ny, nz))

    print(*arr, sep='\n')
    ans = 0
    for height in range(k):
        for row in range(n):
            for col in range(m):
                if arr[height][row][col] == 0:
                    return -1
                ans = max(ans, arr[height][row][col] - 1)

    return ans


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    arr = [[list(map(int, input().split())) for _ in range(m)] for _ in range(k)]
    print(solution(n, m, k, arr))
