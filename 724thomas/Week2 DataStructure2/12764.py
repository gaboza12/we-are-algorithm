# https://www.acmicpc.net/problem/12764

'''
1. 아이디어 :
    힙으로 가장 먼저 나가는 시간과 자리를 저장
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙, 배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(n, use):
    ans = 0
    counter = [0] * len(use)
    min_heap = []
    empty_seats = [i for i in range(len(use))]

    use.sort()

    for start, end in use:
        while min_heap and min_heap[0][0]<start:
            finished, next_seat = heapq.heappop(min_heap)
            heapq.heappush(empty_seats, next_seat)

        next_seat = heapq.heappop(empty_seats)
        counter[next_seat] += 1
        heapq.heappush(min_heap, (end, next_seat))

        ans = max(ans, len(min_heap))

    return [ans, counter[:ans]]


n = int(input())
use = []
for _ in range(n):
    use.append(list(map(int, input().split())))
ans = solution(n, use)
print(ans[0])
print(*ans[1])


