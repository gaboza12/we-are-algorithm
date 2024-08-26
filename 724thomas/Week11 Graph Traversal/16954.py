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
def solution(arr):
    start = [7, 0]
    end = [0, 7]
    dir = [[0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1], [-1, -1], [-1, 0], [-1, 1]]

    def move_walls(walls):
        new_walls = set()
        for x, y in walls:
            if x + 1 < 8:
                new_walls.add((x + 1, y))
        return new_walls

    walls = set()
    for row in range(8):
        for col in range(8):
            if arr[row][col] == "#":
                walls.add((row, col))

    queue = deque([start])

    while queue:
        visited = [[False] * 8 for _ in range(8)]
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x,y) == (0,7):
                return 1

            if (x, y) in walls:
                continue

            for x2, y2 in dir:
                nx, ny = x+x2, y+y2
                if not(0 <= nx < 8 and 0 <= ny < 8) or visited[nx][ny] or (nx, ny) in walls:
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny))
        walls = move_walls(walls)

    return 0

if __name__ == '__main__':
    arr = [list(input().strip()) for _ in range(8)]
    print(solution(arr))
