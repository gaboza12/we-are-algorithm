# https://www.acmicpc.net/problem/2228

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
    concluded = [[0] + [float("-inf")] * m for _ in range(n + 1)]
    notConcluded = [[0] + [float("-inf")] * m for _ in range(n + 1)]

    for i in range(1, n + 1):
        num = arr[i-1]
        for j in range(1, m + 1):
            notConcluded[i][j] = max(concluded[i - 1][j], notConcluded[i - 1][j])
            concluded[i][j] = max(concluded[i - 1][j], notConcluded[i - 1][j - 1]) + num
    return max(concluded[n][m], notConcluded[n][m])

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    print(solution(n, m, arr))


