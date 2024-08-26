# https://www.acmicpc.net/problem/10775

'''
1. 아이디어 :
    union-find
    num[i] = i 인 배열을 만들어놓는다. (num[i] != [i]) 이면 이미 도킹중

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import heapq


def solution(n, m, planes):
    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            par[b] = a

    par = [i for i in range(n + 1)]

    count = 0
    for plane in planes:
        gate = find(plane)
        if gate == 0:
            break
        union(gate - 1, gate)
        count += 1

    return count


n = int(input())
m = int(input())
arr = []
for _ in range(m):
    arr.append(int(input()))
print(solution(n, m, arr))
