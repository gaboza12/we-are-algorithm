# https://www.acmicpc.net/problem/2285

'''
1. 아이디어 :
    누적합과 중앙값 사용
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, towns):
    towns.sort()
    total = sum([towns[i][1] for i in range(len(towns))])
    mid_point = (total+1) // 2
    curr = 0
    for idx, people in towns:
        curr += people
        if curr >= mid_point:
            return idx+1



n = int(input())
towns = []
for _ in range(n):
    towns.append(list(map(int, input().strip().split())))
print(solution(n, towns))
