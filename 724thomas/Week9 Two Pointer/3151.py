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

from collections import Counter


def solution(n, nums):
    # print(*arr, sep="\n")
    nums.sort()
    counter = Counter(nums)
    count = 0

    for i, a in enumerate(nums):
        left, right = i + 1, n - 1
        while left < right:
            total = a + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                if nums[left] == nums[right]:
                    count += right - left
                else:
                    count += counter[nums[right]]
                left += 1
    return count


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().strip().split()))
    print(solution(n, nums))
