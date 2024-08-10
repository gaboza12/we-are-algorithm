# https://www.acmicpc.net/problem/

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


def solution(n, m, r, arr):

    def rotated_cord(layer):  # 0, 1
        nums = []
        for i in range(m - 1 - layer * 2):
            nums.append(arr[layer][i + layer])
        for i in range(n - 1 - layer * 2):
            nums.append(arr[i + layer][-1 - layer])
        for i in range(m - 1 - layer * 2):
            nums.append(arr[-1 - layer][-1 - i - layer])
        for i in range(n - 1 - layer * 2):
            nums.append(arr[-1 - i - layer][layer])

        nums = nums[r:] + nums[:r]

        idx = 0
        for i in range(m - 1 - layer * 2):
            arr[layer][i + layer] = nums[idx]
            idx += 1
        for i in range(n - 1 - layer * 2):
            arr[i + layer][-1 - layer] = nums[idx]
            idx += 1
        for i in range(m - 1 - layer * 2):
            arr[-1 - layer][-1 - i - layer] = nums[idx]
            idx += 1
        for i in range(n - 1 - layer * 2):
            arr[-1 - i - layer][layer] = nums[idx]
            idx += 1

    for i in range(min(n, m) // 2):
        rotated_cord(i)
    # print(*arr, sep='\n')
    for a in arr:
        print(*a)
    return


if __name__ == '__main__':
    n, m, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    solution(n, m, r, arr)
