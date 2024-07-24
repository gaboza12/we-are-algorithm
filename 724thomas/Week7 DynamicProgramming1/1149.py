# https://www.acmicpc.net/problem/1149

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

from collections import deque


def solution(n, arr):
    for i in range(1, len(arr)):
        arr[i][0] += min(arr[i - 1][1], arr[i - 1][2])
        arr[i][1] += min(arr[i - 1][0], arr[i - 1][2])
        arr[i][2] += min(arr[i - 1][0], arr[i - 1][1])

    return min(arr[-1])


if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))
