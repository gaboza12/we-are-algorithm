# https://www.acmicpc.net/problem/1106

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


def solution(c, n, arr):
    cmax = max([x[1] for x in arr])
    dp = [float('inf')] * (c+cmax)
    dp[0] = 0
    arr.sort(key = lambda x: x[1], reverse=True)
    for cost, people in arr:
        for i in range(people, c+cmax):
            dp[i] = min(dp[i], dp[i-people] + cost)

    return min(dp[c:])


if __name__ == '__main__':
    c, n = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(c, n, arr))
