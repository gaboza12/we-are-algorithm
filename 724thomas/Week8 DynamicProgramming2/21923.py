# https://www.acmicpc.net/problem/21923

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

def solution(n, m, arr):
    up = [[0 for _ in range(m)] for _ in range(n)]
    down = [[0 for _ in range(m)] for _ in range(n)]

    up[-1][0], down[-1][-1] = arr[-1][0], arr[-1][-1]
    for row in range(n-2,-1,-1):
        up[row][0] = up[row+1][0] + arr[row][0]
        down[row][-1] = down[row+1][-1] + arr[row][-1]
    for col in range(1, m):
        up[-1][col] = up[-1][col-1] + arr[-1][col]
        down[-1][m-col-1] = down[-1][m-col] + arr[-1][m-col-1]

    for row in range(n-2,-1,-1):
        for col in range(1, m):
            up[row][col] = arr[row][col] + max(up[row+1][col], up[row][col-1])
            down[row][m-col-1] = arr[row][m-col-1] + max(down[row+1][m-col-1], down[row][m-col])

    cmax = -float('inf')
    for row in range(n):
        for col in range(m):
            cmax = max(cmax, up[row][col] + down[row][col])
    return cmax

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    print(solution(n, m, arr))


