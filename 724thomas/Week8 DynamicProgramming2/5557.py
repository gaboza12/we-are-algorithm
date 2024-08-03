# https://www.acmicpc.net/problem/5557

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


def solution(n, arr):
    target = arr.pop()
    prev = defaultdict(int)
    prev[arr[0]] = 1

    for num in arr[1:]:
        curr = defaultdict(int)
        for k, v in prev.items():
            if 0 <= k + num <= 20:
                curr[k + num] += v
            if 0 <= k - num <= 20:
                curr[k - num] += v
        prev = curr
        print(num, prev)
    return prev[target]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr.copy()))
