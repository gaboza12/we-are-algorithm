# https://www.acmicpc.net/problem/2696

'''
1. 아이디어 :
    bigger, smaller 힙을 만들고, mid보다 크면 bigger, 작으면 smaller에 넣고,
    bigger, smaller의 길이를 맞추면서 mid를 갱신
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq


def solution(arr):
    ans = []
    bigger_heap = []
    smaller_heap = []

    mid = arr[0]

    idx = 1
    while idx < len(arr):
        ans.append(mid)
        for _ in range(2):
            if arr[idx] < mid:
                heapq.heappush(smaller_heap, -arr[idx])
            else:
                heapq.heappush(bigger_heap, arr[idx])
            idx += 1

        if len(smaller_heap) < len(bigger_heap):
            heapq.heappush(smaller_heap, -mid)
            mid = heapq.heappop(bigger_heap)
        elif len(smaller_heap) > len(bigger_heap):
            heapq.heappush(bigger_heap, mid)
            mid = -heapq.heappop(smaller_heap)

    ans.append(mid)
    return ans


for _ in range(int(input())):
    n = int(input())
    arr = []
    for _ in range(n // 10 + 1):
        arr += list(map(int, input().strip().split()))
    ans = solution(arr)
    print(len(ans))
    for i in range(0, len(ans), 10):
        print(*ans[i:i + 10])
