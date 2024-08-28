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


def solution(n, m, k, shapes):
    # print(*shapes, sep="\n")

    def rotate(matrix):
        transposed_matrix = [list(row) for row in zip(*matrix)]
        for row in transposed_matrix:
            row.reverse()
        return transposed_matrix

    def change(x, y, matrix):
        row_size, col_size = len(matrix), len(matrix[0])
        for row in range(row_size):
            for col in range(col_size):
                if matrix[row][col]:
                    check_arr[x+row][y+col] = 1

    def check(x, y, matrix):
        row_size, col_size = len(matrix), len(matrix[0])
        if x + row_size > n or y + col_size > m:
            return False
        for row in range(row_size):
            for col in range(col_size):
                if matrix[row][col] == 0: continue
                if check_arr[x+row][y+col]:
                    return False
        change(x, y, matrix)
        return True


    check_arr = [[0] * m for _ in range(n)]

    for shape in shapes:
        inserted = False
        for i in range(4):
            if inserted:
                continue
            for row in range(n):
                for col in range(m):
                    if inserted:
                        continue
                    if check(row, col, shape):
                        inserted = True
                        break

            shape = rotate(shape)
    # print(*check_arr, sep="\n")
    count = 0
    for row in range(n):
        for col in range(m):
            if check_arr[row][col]:
                count+=1
    return count


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    shapes = []
    for _ in range(k):
        row, col = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(row)]
        shapes.append(arr)

    print(solution(n, m, k, shapes))

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
