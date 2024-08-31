# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import deque, defaultdict


def solution(n, h, d, arr):
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    print(*arr, sep="\n")

    def get_distance(x, y, x2, y2):
        return abs(x - x2) + abs(y - y2)

    s = [0, 0]
    e = [0, 0]
    umb = []
    for row in range(n):
        for col in range(n):
            if arr[row][col] == "S":
                s = [row, col]
            elif arr[row][col] == "E":
                e = [row, col]
                umb.append((row, col))
            elif arr[row][col] == "U":
                umb.append((row, col))

    ans = [float('inf')]
    visited = set()
    visited.add((s[0], s[1]))
    cache = {}

    def dfs(x, y, health, dur, steps):
        if x == e[0] and y == e[1]:
            ans[0] = min(ans[0], steps)
            return

        if (x, y, health, dur) in cache and cache[(x, y, health, dur)] <= steps:
            return
        cache[(x, y, health, dur)] = steps

        for x2, y2 in umb:
            if (x2, y2) == (x, y):
                continue
            cost = get_distance(x, y, x2, y2)
            nhealth = health
            ndur = dur

            if ndur < cost:
                nhealth -= (cost - dur)
                ndur = 0
            else:
                ndur -= cost
            if nhealth >= 0:
                if arr[x2][y2] == "U":
                    ndur = d
                dfs(x2, y2, nhealth, ndur, steps + cost)

    dfs(s[0], s[1], h, 0, 0)

    return ans[0] if ans[0] != float('inf') else -1


if __name__ == '__main__':
    n, h, d = map(int, input().split())
    arr = [list(input().strip()) for _ in range(n)]
    print(solution(n, h, d, arr))

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
