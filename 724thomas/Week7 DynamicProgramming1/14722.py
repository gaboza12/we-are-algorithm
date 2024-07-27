# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    curr[2] < curr[0]: 현재 위치에서 우유 2(바나나우유)를 마시기 위해서는 이전 위치에서 우유 0(딸기우유)를 마신 상태보다 더 많은 우유를 마실 수 있는지 확인.
    만약 현재 위치에서 바나나우유를 마시는 것이 이전 상태보다 우유를 더 많이 마실 수 있다면, 그 값을 갱신.
    curr[0] < curr[1]: 현재 위치에서 우유 1(초코우유)을 마시기 위해서는 이전 위치에서 우유 0(딸기우유)를 마신 상태보다 더 많은 우유를 마실 수 있는지 확인.
    만약 현재 위치에서 초코우유를 마시는 것이 이전 상태보다 우유를 더 많이 마실 수 있다면, 그 값을 갱신.
2. 시간복잡도 :
    O(n*n)
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, array):
    def get_prev(n):
        if n == 0:
            return 2
        return n - 1

    # dp 배열 초기화
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

    if array[0][0] == 0:
        dp[0][0][0] = 1

    # 초기 셋팅
    for i in range(1, n):
        milk = array[0][i]
        curr = dp[0][i]
        prev = dp[0][i - 1]
        curr[0] = prev[2] + 1 if milk == 0 else prev[0]
        curr[1] = prev[0] + 1 if milk == 1 and curr[2] < curr[0] else prev[1]
        curr[2] = prev[1] + 1 if milk == 2 and curr[0] < curr[1] else prev[2]

    for i in range(1, n):
        milk = array[i][0]
        curr = dp[i][0]
        prev = dp[i - 1][0]
        curr[0] = prev[2] + 1 if milk == 0 else prev[0]
        curr[1] = prev[0] + 1 if milk == 1 and curr[2] < curr[0] else prev[1]
        curr[2] = prev[1] + 1 if milk == 2 and curr[0] < curr[1] else prev[2]

    # 나머지 DP 테이블 채우기
    for i in range(1, n):
        for j in range(1, n):
            milk = array[i][j]
            curr, left, top = dp[i][j], dp[i][j - 1], dp[i - 1][j]
            curr[0] = max(left[2] + 1, top[2] + 1) if milk == 0 else max(left[0], top[0])
            curr[1] = max(left[0] + 1, top[0] + 1) if milk == 1 and curr[2] < curr[0] else max(left[1], top[1])
            curr[2] = max(left[1] + 1, top[1] + 1) if milk == 2 and curr[0] < curr[1] else max(left[2], top[2])

    return max(dp[n - 1][n - 1])


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))
