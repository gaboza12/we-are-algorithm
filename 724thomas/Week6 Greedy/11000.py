# https://www.acmicpc.net/problem/11000

'''
1. 아이디어 :
    힙으로 풀 수 있다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(n, arr):
    arr.sort()
    cmax = 0
    rooms = []
    for start, end in arr:
        while rooms and rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)
        cmax = max(cmax, len(rooms))

    return cmax

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split())))
print(solution(n, arr))


