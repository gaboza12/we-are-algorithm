# https://www.acmicpc.net/problem/17836

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
import heapq


def solution(n, m, t, arr):
    # print(*arr, sep="\n")
    min_heap = [(0, 0, 0, 0)]  # time, x, y, sword
    visited = set()
    visited.add((0, 0))
    dir = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    while min_heap:
        time, x, y, sword = heapq.heappop(min_heap)
        if time > t:
            continue
        if x == n - 1 and y == m - 1:
            return time

        if sword:
            heapq.heappush(min_heap, (abs(n - 1 - x) + abs(m - 1 - y) + time, n - 1, m - 1, 1))
            continue

        for x2, y2 in dir:
            nx, ny = x + x2, y + y2
            if not (0 <= nx < n and 0 <= ny < m) or (nx, ny) in visited or arr[nx][ny] == 1:
                continue
            visited.add((nx,ny))
            if arr[nx][ny] == 2:
                heapq.heappush(min_heap, (time + 1, nx, ny, 1))
            else:
                heapq.heappush(min_heap, (time + 1, nx, ny, 0))
    return "Fail"


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, m, t, arr))
