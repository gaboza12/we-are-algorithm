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
    print(*arr, sep="\n")

    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    queue = deque()
    queue.append((0, 0, 0, 1))  # x, y, used, time

    while queue:
        print(queue)
        x, y, used, time = queue.popleft()
        if x == n - 1 and y == m - 1:
            return time

        for x2, y2 in dir:
            nx, ny = x + x2, y + y2
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny][used] or arr[nx][ny] == "1":
                continue
            visited[nx][ny][used] = True
            queue.append((nx, ny, used, time+1))

        if not used:
            for x2, y2 in dir:
                nx, ny = x + x2, y + y2
                if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny][1]:
                    continue
                visited[nx][ny][1] = True
                queue.append((nx, ny, 1, time+1))
        print(*visited, sep="\n")
        print()

    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solution(n, m, arr))
