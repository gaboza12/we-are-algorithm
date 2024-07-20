# https://www.acmicpc.net/problem/1374

'''
1. 아이디어 :
    인터벌 문제
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(lectures, arr):
    arr.sort()
    ans = 0
    min_heap = []
    for start, end in arr:
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)
        ans = max(ans, len(min_heap))

    return ans

lectures = int(input())
arr = []
for _ in range(lectures):
    _, start, end = list(map(int, input().strip().split()))
    arr.append((start, end))
print(solution(lectures, arr))


