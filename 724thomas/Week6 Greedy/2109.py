# https://www.acmicpc.net/problem/2109

'''
1. 아이디어 :
    힙을 사용한다.
    3일차에 갈 수 있는 강의는 최대 3개 이기때문에, 3개까지만 유지되어야한다.
    강의날이 3일이고, 스케줄에 추가했는데 총 4개가 있다면, 가장 작은걸 뺀다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(n, lec):
    lec.sort(key = lambda x : x[1])
    min_heap= []
    for pay, day in lec:
        heapq.heappush(min_heap, pay)
        if day < len(min_heap):
            heapq.heappop(min_heap)

    return sum(min_heap)

n = int(input())
lec = [list(map(int, input().strip().split())) for _ in range(n)]

print(solution(n, lec))


