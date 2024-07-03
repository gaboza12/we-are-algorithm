# https://www.acmicpc.net/problem/1068

'''
1. 아이디어 :

2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열, 해시셋
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict
def solution(n, arr, m):
    def dfs(target):
        removed.add(target)
        for child in childs[target]:
            dfs(child)

    childs = defaultdict(set)
    for i in range(len(arr)):
        if arr[i] != -1:
            childs[arr[i]].add(i)

    removed = set()
    dfs(m)

    leafs = 0
    for i in range(n):
        if i not in removed and (i not in childs or len(childs[i] - removed) == 0):
            leafs+=1
    return leafs

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
print(solution(n, arr, m))


