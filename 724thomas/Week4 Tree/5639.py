# https://www.acmicpc.net/problem/5639

'''
1. 아이디어 :
    dfs와 이분탐색으로 풀었다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(nums):

    def dfs(arr):
        if len(arr) == 0:
            return []
        if len(arr) == 1:
            return [arr[0]]

        center = [arr[0]]

        left = 1
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < center[0]:
                left = mid + 1
            else:
                right = mid

        left = dfs(arr[1:right])
        right = dfs(arr[right:])
        return left+right+center

    return dfs(nums)


nums = []
while True:
    try:
        nums.append(int(sys.stdin.readline()))
    except:
        break
ans = solution(nums)
for a in ans:
    print(a)
