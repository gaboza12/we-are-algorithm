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


def solution(n, m, r, arr, at, df):
    print(*arr, sep="\n")
    print(at)
    print(df)

    directions = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
    visited = set()
    ans = [0]

    def update():
        for row in range(n):
            for col in range(m):
                arr[row][col] = "F" if (row, col) in visited else "S"

    def push(x, y, dir):
        if (x, y) in visited:
            return
        visited.add((x, y))
        x2, y2 = directions[dir]
        counts = arr[x][y]-1
        ans[0] += 1

        while counts:
            x, y = x + x2, y + y2
            if not (x in range(n) and y in range(m)):
                return
            if (x,y) not in visited:
                visited.add((x, y))
                ans[0] += 1
                counts = max(counts - 1, arr[x][y]-1)
            else:
                counts-=1


    for i in range(r):
        row, col, dir = at[i]
        push(int(row) - 1, int(col) - 1, dir)
        row, col = df[i]
        visited.discard((int(row) - 1, int(col) - 1))
        print(visited)

    update()
    print(ans[0])
    for row in arr:
        print(*row)


if __name__ == '__main__':
    n, m, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    at, df = [], []
    for _ in range(r):
        at.append(list(input().split()))
        df.append(list(input().split()))

    solution(n, m, r, arr, at, df)

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
