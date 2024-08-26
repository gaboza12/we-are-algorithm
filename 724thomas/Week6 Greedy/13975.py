# https://www.acmicpc.net/problem/13975

'''
1. 아이디어 :
    힙을 사용한다
2. 시간복잡도 :
    O( nlog n)
3. 자료구조 :
    힙
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq


def solution(n, arr):
    heapq.heapify(arr)
    cost = 0
    while len(arr) >= 2:
        left, right = heapq.heappop(arr), heapq.heappop(arr)
        heapq.heappush(arr, left+right)
        cost += left+right

    return cost


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))
