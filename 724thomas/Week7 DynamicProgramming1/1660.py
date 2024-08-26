# https://www.acmicpc.net/problem/1660

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


def solution(n):
    triangle = [1, 3, 6, 10]
    top = [1, 4, 10, 20]
    while top[-1] <= n:
        triangle.append(triangle[-1] + len(triangle) + 1)
        top.append(top[-1] + triangle[-1])

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for num in top:
        for i in range(num, n + 1):
            dp[i] = min(dp[i], dp[i - num] + 1)
    return dp[-1]


if __name__ == '__main__':
    print(solution(int(input())))
