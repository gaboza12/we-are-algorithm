# https://www.acmicpc.net/problem/11286

'''
1. 아이디어 :
    heapq 사용
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
def solution(commands):
    min_heap = []
    for command in commands:
        if command == 0:
            if len(min_heap) == 0:
                print(0)
            else:
                print(heapq.heappop(min_heap)[1])
        else:
            heapq.heappush(min_heap, (abs(command), command))

n = int(input())
commands = []
for _ in range(n):
    commands.append(int(input()))
solution(commands)


