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


def solution(n, l, r, arr):
    # print(*arr, sep="\n")

    visited = set()
    count = 0
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    cand = deque()
    for i in range(n):
        for j in range(i % 2, n, 2):
            cand.append((i, j))

    def bfs(row, col):
        visited.add((row, col))
        queue = deque()
        queue.append((row, col))
        changes = set()
        changes.add((row, col))
        total = arr[row][col]

        while queue:
            x, y = queue.popleft()

            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < n) \
                        or (nx, ny) in visited \
                        or not (l <= abs(arr[nx][ny] - arr[x][y]) <= r):
                    continue
                visited.add((nx, ny))
                changes.add((nx, ny))
                total += arr[nx][ny]
                queue.append((nx, ny))

        return changes, total

    moved = True
    count = -1
    while moved:
        count += 1
        moved = False
        visited = set()
        for row in range(n):
            for col in range(n):
                if (row, col) not in visited:
                    changes, total = bfs(row, col)
                    print(changes, total)
                    if len(changes) != 1:
                        moved = True
                    pop = total // len(changes)
                    for row2, col2 in changes:
                        arr[row2][col2] = pop
    print(*arr, sep='\n')
    return count


if __name__ == '__main__':
    n, l, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, l, r, arr))
