# https://www.acmicpc.net/problem/15691

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

from collections import defaultdict


def solution(n, d, length, coupon, sushi):
    sushi += sushi
    hmap = defaultdict(int)
    hmap[coupon] += 1
    kinds = 1
    ans = 1
    left = 0
    for right in range(length):
        hmap[sushi[right]] += 1
        if hmap[sushi[right]] == 1:
            kinds += 1
    ans = max(ans, kinds)
    right += 1
    while right < len(sushi):
        hmap[sushi[right]] += 1
        if hmap[sushi[right]] == 1:
            kinds += 1
        hmap[sushi[left]] -= 1
        if hmap[sushi[left]] == 0:
            kinds -= 1
        left += 1
        right += 1
        ans = max(ans, kinds)

    return ans


if __name__ == '__main__':
    n, d, k, c = list(map(int, input().split()))
    arr = [int(input()) for _ in range(n)]
    # arr = list(map(int, input().strip().split()))
    print(solution(n, d, k, c, arr))
