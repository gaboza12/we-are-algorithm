# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, k, nums):
    left = 0
    right = 0
    odd_count = 0
    ans = 0
    while right < len(nums):
        if nums[right] % 2:  # 홀수
            odd_count += 1
            while k < odd_count:
                if nums[left] % 2:
                    odd_count -= 1
                left += 1
        ans = max(ans, right - left - odd_count +1)
        right += 1

    return ans


n, k = list(map(int, input().split()))
arr = list(map(int, input().strip().split()))
print(solution(n, k, arr))
