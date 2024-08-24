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

    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    pqueue = deque()
    fqueue = deque()
    visited = set()

    for row in range(n):
        for col in range(m):
            if arr[row][col] == "J":
                pqueue.append((row, col))
                visited.add((row, col))
            elif arr[row][col] == "F":
                fqueue.append((row, col))

    count = 0
    while pqueue:
        temp_fqueue = deque()
        for x, y in fqueue:
            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == "F" or arr[nx][ny] == "#":
                    continue
                arr[nx][ny] = "F"
                temp_fqueue.append((nx, ny))

        temp_pqueue = deque()
        for x, y in pqueue:
            if (x == 0 or x == n - 1 or y == 0 or y == m - 1) and arr[x][y] != "#":
                return count + 1

            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or (nx, ny) in visited or arr[nx][ny] == "#" or arr[nx][ny] == "F":
                    continue
                visited.add((nx, ny))
                temp_pqueue.append((nx, ny))


        pqueue = temp_pqueue
        fqueue = temp_fqueue
        count += 1
        # print(*arr, sep="\n")
        # print(pqueue)

    return "IMPOSSIBLE"


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solution(n, m, arr))
