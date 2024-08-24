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

from itertools import combinations
from collections import deque


def solution(n, m, arr):

    def spread():
        queue = deque(virus)
        temp_arr = [row[:] for row in arr]
        temp_empty = len(empty)

        while queue:
            x, y = queue.popleft()

            for x2, y2 in dir:
                nx, ny = x + x2, y + y2

                if not (0 <= nx < n and 0 <= ny < m) or temp_arr[nx][ny] != 0:
                    continue
                temp_arr[nx][ny] = 2
                queue.append((nx, ny))
                temp_empty -= 1
                if temp_empty <= ans:
                    return 0
        return temp_empty - 3

    virus = []
    empty = []
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    for row in range(n):
        for col in range(m):
            if arr[row][col] == 2:
                virus.append((row, col))
            elif arr[row][col] == 0 :
                empty.append((row, col))

    ans = 0

    for walls in combinations(empty, 3):
        for x, y in walls:
            arr[x][y] = 1

        safe = spread()
        ans = max(ans, safe)

        for x, y in walls:
            arr[x][y] = 0

    return ans


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, arr))
