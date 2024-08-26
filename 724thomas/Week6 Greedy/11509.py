# https://www.acmicpc.net/problem/11509

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, arr):
    arrows = defaultdict(int)
    count = 0
    for height in arr:
        if arrows[height] > 0:
            arrows[height] -= 1
            arrows[height - 1] += 1
        else:
            count += 1
            arrows[height - 1] += 1
    return count


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))
