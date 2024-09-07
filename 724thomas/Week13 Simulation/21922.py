# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, arr, start):
    wind_dirs = {1: [2, 1, 0, 3], 2: [0, 3, 2, 1], 3: [3, 2, 1, 0], 4: [1, 0, 3, 2]}
    move_dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def change_wind(dir, value):
        return wind_dirs[value][dir]

    def bfs(x, y):
        visited.add((x, y))

        for d in range(4):
            nx, ny = x + move_dirs[d][0], y + move_dirs[d][1]

            while 0 <= nx < n and 0 <= ny < m:
                visited.add((nx, ny))

                if arr[nx][ny] == 0:
                    nx = nx + move_dirs[d][0]
                    ny = ny + move_dirs[d][1]
                elif arr[nx][ny] == 9:
                    break
                else:
                    d = change_wind(d, arr[nx][ny])
                    nx = nx + move_dirs[d][0]
                    ny = ny + move_dirs[d][1]

    visited = set()

    for x, y in start:
        bfs(x, y)

    return len(visited)


if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    start = []
    for row in range(n):
        temp = list(map(int, input().split()))
        for col in range(m):
            if temp[col] == 9:
                start.append([row,col])
        arr.append(temp)
    print(solution(n, m, arr, start))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
