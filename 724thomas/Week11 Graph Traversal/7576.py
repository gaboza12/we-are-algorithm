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
    queue = deque()
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 1:
                queue.append((row, col))

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while queue:
        x, y = queue.popleft()
        next_val = arr[x][y] + 1

        for x2, y2 in dir:
            nx, ny = x + x2, y + y2
            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] != 0:
                continue
            arr[nx][ny] = next_val
            queue.append((nx, ny))

    ans = 0
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 0:
                return -1
            ans = max(ans, arr[row][col]-1)

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, m, arr))
