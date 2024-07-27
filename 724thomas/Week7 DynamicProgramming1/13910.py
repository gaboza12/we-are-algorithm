# https://www.acmicpc.net/problem/13910

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

from itertools import permutations
import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(n, m, arr):
    nums = set(arr)
    for perms in permutations(arr, 2):
        nums.add(sum(perms))

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for num in nums:
        for i in range(num, n + 1):
            dp[i] = min(dp[i], dp[i - num] + 1)
    return dp[-1] if dp[n] != float('inf') else -1


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().strip().split()))
    print(solution(n, m, arr))
