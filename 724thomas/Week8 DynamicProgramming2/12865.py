# https://www.acmicpc.net/problem/12865

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


def solution(n, k, arr):
    arr.sort()
    dp = [0] * (k+1)
    for weight, value in arr:
        temp = dp.copy()
        for i in range(weight, k+1):
            temp[i] = max(temp[i], dp[i-weight] + value)
        dp = temp
    return max(dp)


if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, k, arr))
