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

def solution(arr):
    dp = [[0]*2001 for i in range(11)]
    dp[0] = [1]*2001
    for i in range(1, 11):
        for j in range(1, 2001):
            dp[i][j] = dp[i][j-1]+dp[i-1][j//2]

    for n, m in arr:
        print(dp[n][m])

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(int, input().strip().split())))
    solution(arr)
