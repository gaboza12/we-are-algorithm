# https://www.acmicpc.net/problem/9489

'''
1. 아이디어 :
    부모 배열을 만들고, 조부모가 같고 부모가 다르면 카운트
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배ㅐ열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, k, arr):
    a = [-1] + arr
    parent = [0] * (n + 1)
    parent[0] = -1
    target = 0
    idx = -1
    for i in range(1, n + 1):
        if a[i] == k:
            target = i
        if a[i] != a[i - 1] + 1:
            idx += 1
        parent[i] = idx
    answer = 0
    print(parent)
    for i in range(1, n + 1):
        if parent[i] != parent[target] and parent[parent[i]] == parent[parent[target]]:
            answer += 1
    return answer

while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        exit()
    arr = list(map(int, input().split()))
    print(solution(n, m, arr))
