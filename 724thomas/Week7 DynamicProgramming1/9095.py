# https://www.acmicpc.net/problem/9095

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

1, 2, 4, 7, 13, 24, 44,
def solution(nums):
    dp = [0] * (12)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 12):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    for n in nums:
        print(dp[n])

nums = []
for _ in range(int(input())):
    nums.append(int(input()))
solution(nums)


