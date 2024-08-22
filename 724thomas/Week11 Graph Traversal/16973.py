# https://www.acmicpc.net/problem/16973

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


def solution(n, m, arr, vars):
    height = vars[0]
    width = vars[1]
    start_x, start_y = vars[2] - 1, vars[3] - 1

    for row in range(n):
        for col in range(m):
            if arr[row][col] == 1:
                for i in range(row, max(-1, row - height), -1):
                    for j in range(col, max(-1, col - width), -1):
                        arr[i][j] = 1

    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = deque()
    queue.append([start_x, start_y, 0])
    arr[start_x][start_y] = 1

    while queue:
        x, y, time = queue.popleft()
        if x == vars[4] - 1 and y == vars[5] - 1:
            return time

        for x2, y2 in dir:
            nx, ny = x + x2, y + y2
            if not (0 <= nx < n - height + 1 and 0 <= ny < m - width + 1) or arr[nx][ny] == 1:
                continue
            arr[nx][ny] = 1
            queue.append((nx, ny, time + 1))

    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    vars = list(map(int, input().split()))
    print(solution(n, m, arr, vars))
