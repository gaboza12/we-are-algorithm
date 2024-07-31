# https://www.acmicpc.net/problem/15724

'''
1. 아이디어 :
    누적합
2. 시간복잡도 :
    O( n*m )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, arr, cords):
    print(*arr, sep="\n")
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    print()
    dp[1][1] = arr[0][0]
    for i in range(1, n):
        dp[i+1][1] = dp[i][1] + arr[i][0]
    for i in range(1, m):
        dp[1][i+1] = dp[1][i] + arr[0][i]
    for row in range(1, n):
        for col in range(1, m):
            dp[row+1][col+1] = arr[row][col] + dp[row][col+1] + dp[row+1][col] - dp[row][col]

    for x1, y1, x2, y2 in cords:
        print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))

    cords = []
    for _ in range(int(input())):
        cords.append(list(map(int, input().strip().split())))
    solution(n, m, arr, cords)
