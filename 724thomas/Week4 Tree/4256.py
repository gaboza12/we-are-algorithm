# https://www.acmicpc.net/problem/4256

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( n^2 )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, pre_order, in_order):

    def dfs(pre_order, in_order):
        if not pre_order or not in_order:
            return []

        mid = pre_order[0]
        idx = in_order.index(mid)

        in_left = in_order[:idx]
        in_right = in_order[idx+1:]
        pre_left = pre_order[1:len(in_left)+1]
        pre_right = pre_order[len(in_left)+1:]

        left = dfs(pre_left, in_left)
        right = dfs(pre_right, in_right)
        return left + right + [mid]

    return dfs(pre_order, in_order)


for _ in range(int(input())):
    n = int(input())
    pre_order = list(map(int, input().strip().split()))
    in_order = list(map(int, input().strip().split()))
    print(*solution(n, pre_order, in_order))
