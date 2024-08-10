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


def solution(n, arr):
    arr.sort()
    left = 0
    right = n - 1

    cmin = float('inf')
    ans = [0, 0]
    while left < right:
        total = abs(arr[left] + arr[right])
        if total < cmin:
            ans = [arr[left], arr[right]]
            cmin = total
        if arr[left] + arr[right] == 0:
            return ans
        if arr[left] + arr[right] > 0:
            right -= 1
        elif arr[left] + arr[right] < 0:
            left += 1
    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(*solution(n, arr))
