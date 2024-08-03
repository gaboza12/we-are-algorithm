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
import heapq


def solution(n, m, arr):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    queue = []
    queue.append((-arr[0][0], 0, 0))
    visited = set()
    visited.add((0, 0))
    while queue:
        curr, row, col = heapq.heappop(queue)
        for row2, col2 in dir:
            nrow, ncol = row + row2, col + col2
            if not (0 <= nrow < n and 0 <= ncol < m) or arr[nrow][ncol] >= arr[row][col]:
                continue
            if (nrow, ncol) in visited:
                dp[nrow][ncol] += dp[row][col]
                continue
            visited.add((nrow, ncol))
            dp[nrow][ncol] += dp[row][col]
            heapq.heappush(queue, (-arr[nrow][ncol], nrow, ncol))
    return dp[-1][-1]


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    print(solution(n, m, arr))
