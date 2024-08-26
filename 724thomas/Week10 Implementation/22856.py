# https://www.acmicpc.net/problem/22856

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict
def solution(n, childs, pars):

    visited = set()
    ans = [0]
    def dfs_total(curr):
        if childs[curr][0] != -1:
            dfs_total(childs[curr][0])
            ans[0] += 2
        if childs[curr][1] != -1:
            dfs_total(childs[curr][1])
            ans[0] += 2

    def dfs_depth(curr):
        if childs[curr][1] != -1:
            dfs_depth(childs[curr][1])
            ans[0] -= 1


    dfs_total(1)
    dfs_depth(1)
    return ans[0]



if __name__ == '__main__':
    childs = defaultdict(list)
    pars = defaultdict(int)
    n = int(input())
    for _ in range(n):
        par, left, right = list(map(int, input().strip().split()))
        childs[par] = [left, right]
        if left != -1:
            pars[left] = par
        if right != -1:
            pars[right] = par

    print(solution(n, childs, pars))


