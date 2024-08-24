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

from collections import deque
import heapq

def solution(n, m):
    min_heap = []
    heapq.heappush(min_heap, (0,n))
    visited = set()
    visited.add(n)

    while min_heap:
        time, curr = heapq.heappop(min_heap)
        if curr == m:
            return time

        if curr * 2 <= 100000 and curr * 2 not in visited:
            visited.add(curr * 2)
            heapq.heappush(min_heap, (time, curr*2))

        if curr + 1 <= 100000 and curr + 1 not in visited:
            visited.add(curr + 1)
            heapq.heappush(min_heap, (time+1, curr+1))

        if curr - 1 >= 0 and curr - 1 not in visited:
            visited.add(curr - 1)
            heapq.heappush(min_heap, (time+1, curr-1))


if __name__ == '__main__':
    n, m = map(int, input().split())
    # arr = tuple(map(int, input().split()))
    print(solution(n, m))
