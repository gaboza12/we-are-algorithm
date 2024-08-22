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

from collections import defaultdict


def solution(grid, arr):
    rows_count = {i: 5 for i in range(5)}
    cols_count = {i: 5 for i in range(5)}
    neg_diag = 5
    pos_diag = 5
    row_idx = defaultdict(int)
    col_idx = defaultdict(int)
    for row in range(5):
        for col in range(5):
            num = grid[row][col]
            row_idx[num] = row
            col_idx[num] = col

    ans = 0
    for i, n in enumerate(arr):
        row = row_idx[n]
        col = col_idx[n]
        rows_count[row] -= 1
        cols_count[col] -= 1
        if row == col:
            pos_diag -= 1
        if row == 4 - col:
            neg_diag -= 1


        if rows_count[row] == 0:
            rows_count[row] = -1
            ans += 1
        if cols_count[col] == 0:
            cols_count[col] = -1
            ans += 1
        if pos_diag == 0:
            pos_diag = -1
            ans += 1
        if neg_diag == 0:
            neg_diag = -1
            ans += 1
        if ans >= 3:
            return i+1


if __name__ == '__main__':
    # n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(5)]
    arr = []
    for _ in range(5):
        val = list(map(int, input().split()))
        for n in val:
            arr.append(n)
    print(solution(grid, arr))
