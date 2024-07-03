# https://www.acmicpc.net/problem/14267

'''
1. 아이디어 :
    dfs로 풀 수 있다
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict

def solution(n, m, par, compliments):
    tree = defaultdict(list)
    for i in range(1, n+1):
        parent = par[i-1]
        tree[parent].append(i)


    comp = [0] * (n+1)
    for node, compliment in compliments:
        comp[node] += compliment

    def dfs(node, acc):
        acc += comp[node]
        comp[node] = acc
        for child in tree[node]:
            dfs(child, acc)

    dfs(1, 0)

    return comp[1:]


n, m = list(map(int, input().split()))
par = list(map(int, input().split()))
compliments = []
for _ in range(m):
    compliments.append(list(map(int, input().split())))
print(*solution(n, m, par, compliments))
