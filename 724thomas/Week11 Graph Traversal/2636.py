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
    # print(*arr, sep="\n")

    dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def check(x, y):
        for x2, y2 in dir:
            nx, ny = x + x2, y + y2
            if (nx, ny) in outer:
                return True
        return False

    def get_outer():
        visited = set()
        queue = deque()
        queue.append((0, 0))

        while queue:
            x, y = queue.popleft()

            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or (nx, ny) in visited or arr[nx][ny] == 1:
                    continue
                visited.add((nx, ny))
                queue.append((nx, ny))
        return visited

    candid = set()

    for row in range(1, n - 1):
        for col in range(1, m - 1):
            if arr[row][col]:
                candid.add((row, col))

    cmin = len(candid)
    time = 0
    while candid:
        time += 1
        cmin = min(cmin, len(candid))
        removed = set()
        outer = get_outer()
        for row, col in candid:
            if check(row, col):
                removed.add((row, col))
        for row, col in removed:
            candid.remove((row, col))
            arr[row][col] = 0

    print(time)
    print(cmin)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, arr)
