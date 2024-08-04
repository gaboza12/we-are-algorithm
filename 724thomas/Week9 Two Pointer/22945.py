# https://www.acmicpc.net/problem/22945

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
    # print(*arr, sep="\n")
    print(arr)
    left = 0
    right = n - 1
    cmax = 0
    while left < right:
        cmax = max(cmax, (right - left - 1) * min(arr[left], arr[right]))
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return cmax


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))
