# https://www.acmicpc.net/problem/1915

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

    cmax = 0
    for row in range(n):
        for col in range(m):
            if arr[row][col] == 1:
                cmax = 1
                break

    for row in range(1, n):
        for col in range(1, m):
            if arr[row][col] == 0:
                continue
            arr[row][col] = min(arr[row-1][col-1], arr[row-1][col], arr[row][col-1]) + 1
            cmax = max(cmax, arr[row][col])

    print(*arr, sep="\n")
    return cmax ** 2

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip())))
    print(solution(n, m, arr))


