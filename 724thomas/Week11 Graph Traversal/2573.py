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


def solution(n, m, arr):
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(row, col, negative):
        queue = deque()
        queue.append((row, col))

        while queue:
            x, y = queue.popleft()

            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 0:
                    continue
                if negative and arr[nx][ny] > 0:
                    continue
                if not negative and arr[nx][ny] < 0:
                    continue
                arr[nx][ny] *= -1
                queue.append((nx, ny))
        return 1

    def get_lands(negative):
        land = 0
        for row in range(n):
            for col in range(m):
                if arr[row][col] == 0:
                    continue
                if not negative and arr[row][col] < 0:
                    continue
                if negative and arr[row][col] > 0:
                    continue
                land += bfs(row, col, negative)
        return land

    def melt(negative):
        melted = set()
        for row in range(n):
            for col in range(m):
                if arr[row][col] == 0:
                    continue
                value = arr[row][col]
                for row2, col2 in dir:
                    nr, nc = row + row2, col + col2
                    if not (0 <= nr < n and 0 <= nc < m):
                        continue
                    if arr[nr][nc] == 0:
                        if negative:
                            value += 1
                            if value >= 0:
                                melted.add((row,col))
                            else:
                                arr[row][col] = value
                        else:
                            value -= 1
                            if value <= 0:
                                melted.add((row,col))
                            else:
                                arr[row][col] = value
        for row, col in melted:
            arr[row][col] = 0


    negative = False
    time = 0
    while True:
        land = get_lands(negative)
        if land == 0:
            return 0
        elif land >= 2:
            return time

        negative = not negative
        melt(negative)
        time += 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))
