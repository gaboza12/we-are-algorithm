# https://www.acmicpc.net/problem/4347

'''
1. 아이디어 :
    X, O 개수 차이 0~1
    X와 O 둘다 빙고X
    X 빙고이면 X와 O의 개수 차이 = 1
    O 빙고이면 X와 O의 개수 차이 = 0
2. 시간복잡도 :
    O( 2 * 3 * 3 )
3. 자료구조 :
    -
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(grid):
    def check_counts(base):
        count = 0
        for row in range(3):
            for col in range(3):
                if grid[row][col] == base:
                    count += 1
        return count

    def check_bingo(base):
        for i in range(3):
            if (grid[i][0] == grid[i][1] == grid[i][2] == base) or (grid[0][i] == grid[1][i] == grid[2][i] == base):
                return True

        if (grid[0][0] == grid[1][1] == grid[2][2] == base) or (grid[0][2] == grid[1][1] == grid[2][0] == base):
            return True

        return False

    x_count = check_counts("X")
    o_count = check_counts("O")
    x_has_bingo = check_bingo("X")
    o_has_bingo = check_bingo("O")
    if not (0 <= x_count - o_count <= 1):
        return "no"
    if x_has_bingo and o_has_bingo:
        return "no"
    if x_has_bingo and x_count == o_count:
        return "no"
    if o_has_bingo and x_count == o_count + 1:
        return "no"

    return "yes"


for _ in range(int(input())):
    grid = []
    for _ in range(3):
        grid.append(list(input().strip()))
    print(solution(grid))
    input()
