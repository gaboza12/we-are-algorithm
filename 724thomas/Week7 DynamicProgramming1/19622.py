# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):
    if len(arr) == 1:
        return arr[0][2]
    if len(arr) == 2:
        return max(arr[0][2], arr[1][2])
    dp = [0] * n
    dp[0] = arr[0][2]
    dp[1] = max(arr[0][2], arr[1][2])
    for i in range(2, n):
        dp[i] = max(dp[i-2] + arr[i][2], dp[i-1])
    print(dp)
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))