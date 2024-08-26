# https://www.acmicpc.net/problem/1715

'''
1. 아이디어 :
    최소힙을 사용한다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq

def solution(n, nums):
    ans = 0
    heapq.heapify(nums)
    while len(nums) >= 2:
        left = heapq.heappop(nums)
        right = heapq.heappop(nums)
        heapq.heappush(nums, left+right)
        ans += left+right

    return ans


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(solution(n, nums))
