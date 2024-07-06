# https://www.acmicpc.net/problem/7662

'''
1. 아이디어 :
    두개의 힙을 사용
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :

'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
from collections import defaultdict
def solution(n, commands):

    min_heap = []
    max_heap = []
    counter = defaultdict(int)

    for c, v in commands:
        if c == "I":
            heapq.heappush(min_heap, v)
            heapq.heappush(max_heap, -v)
            counter[v] += 1
        elif c == "D":
            if v == 1:
                while max_heap and counter[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    val = heapq.heappop(max_heap)
                    counter[-val] -= 1
            elif v == -1:
                while min_heap and counter[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    val = heapq.heappop(min_heap)
                    counter[val] -= 1

        while max_heap and counter[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        while min_heap and counter[min_heap[0]] == 0:
            heapq.heappop(min_heap)

    if max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")


for _ in range(int(input())):
    n = int(input())
    commands = []
    for _ in range(n):
        commands.append(list(input().split()))
        commands[-1][1] = int(commands[-1][1])
    solution(n, commands)



