# https://www.acmicpc.net/problem/1022

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
input = lambda: sys.stdin.readline().rstrip()



def solution(x1, y1, x2, y2):

    def get_value(x, y):
        n = max(abs(x), abs(y))
        side_len = 2 * n + 1
        cmax = side_len ** 2
        if x == n:
            return cmax - (n - y)
        elif y == -n:
            return cmax - side_len + 1 - (n - x)
        elif x == -n:
            return cmax - 2 * side_len + 2 - (n + y)
        elif y == n:
            return cmax - 3 * side_len + 3 - (n + x)

    grid = []
    max_val_len = 0

    for i in range(x1, x2 + 1):
        grid.append([])
        for j in range(y1, y2 + 1):
            val = get_value(i, j)
            grid[-1].append(val)
            max_val_len = max(max_val_len, len(str(val)))

    for row in grid:
        print(" ".join(str(x).rjust(max_val_len) for x in row))

if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, input().split())
    solution(x1, y1, x2, y2)
