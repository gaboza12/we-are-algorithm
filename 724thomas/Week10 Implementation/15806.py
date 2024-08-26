# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def solution(n, virus, checks, t):
    # print(*arr, sep="\n")
    dir = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    board = [[[False, False] for _ in range(n)] for _ in range(n)]
    queue = deque()
    for x, y in virus:
        board[x - 1][y - 1][0] = True  # 짝수날 곰팡이 있다.
        queue.append((x - 1, y - 1, 0))

    while queue:
        x, y, day = queue.popleft()
        if day >= t:
            continue
        flag = False
        # 다음 곰팡이 위치
        for dx, dy in dir:
            nx = dx + x
            ny = dy + y
            # 범위내에 위치하면

            if 0 <= nx < n and 0 <= ny < n:
                n_day = (day + 1) % 2
                if board[nx][ny][n_day] == True:
                    continue  # 다음날도 바이러스가 있음
                board[nx][ny][n_day] = True
                queue.append((nx, ny, day + 1))
                flag = True

        if not flag:
            board[x][y][day % 2] = False

    che_odd = t % 2
    # print(board)
    for x, y in checks:
        if board[x - 1][y - 1][che_odd] == True:
            return "YES"
    return "NO"


if __name__ == '__main__':
    n, m, k, t = map(int, input().split())
    virus = [list(map(int, input().strip().split())) for _ in range(m)]
    checks = [list(map(int, input().strip().split())) for _ in range(k)]

    print(solution(n, virus, checks, t))

