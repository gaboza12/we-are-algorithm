# https://www.acmicpc.net/problem/11048

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

    for i in  range(1, n):
        arr[i][0] += arr[i-1][0]
    for i in range(1, m):
        arr[0][i] += arr[0][i-1]

    for row in range(1, n):
        for col in range(1, m):
            arr[row][col] += max(arr[row-1][col-1], arr[row][col-1], arr[row-1][col])
    return arr[-1][-1]

if __name__ == '__main__':
    arr = []
    n, m =list(map(int, input().split()))
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(solution(n, m, arr))


