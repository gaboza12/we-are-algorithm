# https://www.acmicpc.net/problem/21939

'''
1. 아이디어 :
    거지같은 문제
    두개의 힙과 배열을 사용
    새로운 문제는 배열에 추가하고, 푼 문제는 배열에서 지운다.
    추천할때 배열에 있는 레벨을 통해 난이도가 같은지 확인
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    힙, 배열
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq
from collections import defaultdict
def solution(initial, commands):
    def recommend_problem(minHeap, maxHeap, solved, x):
        if x == 1:
            while maxHeap and solved.get(-maxHeap[0][1]) != -maxHeap[0][0]:
                heapq.heappop(maxHeap)
            if maxHeap:
                return -maxHeap[0][1]
        else:
            while minHeap and solved.get(minHeap[0][1]) != minHeap[0][0]:
                heapq.heappop(minHeap)
            if minHeap:
                return minHeap[0][1]

    def add_problem(minHeap, maxHeap, solved, p, l):
        heapq.heappush(minHeap, (l, p))
        heapq.heappush(maxHeap, (-l, -p))
        solved[p] = l

    def solve_problem(solved, p):
        if p in solved:
            del solved[p]

    minHeap = []
    maxHeap = []
    solved = defaultdict(int)

    for q, d in initial:
        add_problem(minHeap, maxHeap, solved, q, d)

    results = []

    for command in commands:
        if command[0] == "recommend":
            x = command[1]
            result = recommend_problem(minHeap, maxHeap, solved, x)
            print(result)
        elif command[0] == "add":
            p = command[1]
            l = command[2]
            add_problem(minHeap, maxHeap, solved, p, l)
        elif command[0] == "solved":
            p = command[1]
            solve_problem(solved, p)


initial = []
for _ in range(int(input())):
    initial.append(list(map(int, input().split())))
commands = []
for _ in range(int(input())):
    commands.append(list(input().split()))
    for i in range(1, len(commands[-1])):
        commands[-1][i] = int(commands[-1][i])
solution(initial, commands)


