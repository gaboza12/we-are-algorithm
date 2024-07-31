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


def solution(d, p, arr):
    dp = [0] * (d + 1)
    dp[0] = float('inf')  # 시작점에서 용량 무한대로 설정

    for distance, capacity in arr:
        for i in range(d, distance - 1, -1):
            dp[i] = max(dp[i], min(dp[i - distance], capacity))

    return dp[d]


if __name__ == '__main__':
    d, p = list(map(int, input().strip().split()))
    arr = []
    for _ in range(p):
        arr.append(list(map(int, input().strip().split())))
    print(solution(d, p, arr))
