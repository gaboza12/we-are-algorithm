# https://www.acmicpc.net/problem/2056

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

def solution(n, arr):
    # print(*arr, sep='\n')
    dp = [0] * (n+1)
    for i in range(1, n+1):
        work, count, *pre = map(int, arr[i-1])
        dp[i] = work
        for j in pre:
            dp[i] = max(dp[i], dp[j] + work)
    return max(dp)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))
