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


def solution(k, m, n, arr):
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    k_dir = [[2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [1, 2], [-1, -2], [1, -2]]
    queue = deque()
    queue.append((0, 0, 0, k))
    visited = set()
    visited.add((0, 0, k))

    while queue:
        # print(queue)
        x, y, time, left = queue.popleft()
        if x == n - 1 and y == m - 1:
            return time

        for x2, y2 in dir:
            nx, ny = x + x2, y + y2
            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 1 or (nx, ny, left) in visited:
                continue
            visited.add((nx, ny, left))
            queue.append((nx, ny, time + 1, left))

        if left:
            for x2, y2 in k_dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == 1 or (nx, ny, left-1) in visited:
                    continue
                visited.add((nx, ny, left-1))
                queue.append((nx, ny, time + 1, left - 1))

    return -1


if __name__ == '__main__':
    k = int(input())
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    print(solution(k, n, m, arr))
