# https://www.acmicpc.net/problem/1655

'''
1. 아이디어 :
    짝수일떄, 홀수일때를 나눠서 힙에 넣고, 두 힙의 길이를 평등하게 유지
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
    is_even = False
    min_heap = []
    max_heap = [-arr[0]]
    print(arr[0])
    for n in arr[1:]:
        if n < -max_heap[0]:
            heapq.heappush(max_heap, -n)
        else:
            heapq.heappush(min_heap, n)
        is_even = not is_even

        if is_even:
            while len(min_heap) != len(max_heap):
                if len(min_heap) > len(max_heap):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
                else:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
        else:
            while len(min_heap)+1 != len(max_heap):
                if len(min_heap)+1 > len(max_heap):
                    heapq.heappush(max_heap, -heapq.heappop(min_heap))
                else:
                    heapq.heappush(min_heap, -heapq.heappop(max_heap))
        print(-max_heap[0])

arr = []
for _ in range(int(input())):
    arr.append(int(input()))
solution(arr)


