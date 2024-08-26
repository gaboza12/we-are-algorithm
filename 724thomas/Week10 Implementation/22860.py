# https://www.acmicpc.net/problem/22860

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import defaultdict, deque


def solution(n, m, arr, queries):
    def add_maps(map1, map2):
        map = defaultdict(int)
        for k, v in map1.items():
            map[k] += v
        for k, v in map2.items():
            map[k] += v
        return map

    degrees = defaultdict(int)
    pars = defaultdict(set)
    childs = defaultdict(str)
    files = {}

    for par, child, type in arr:
        pars[par].add((child, type))
        childs[child] = par
        if type == "1":
            if child not in degrees:
                degrees[child] = 0
            degrees[par] += 1
        elif type == "0":
            if par not in files:
                files[par] = defaultdict(int)
            files[par][child] += 1

    queue = deque(k for k, v in degrees.items() if v == 0)

    while queue:
        child = queue.popleft()
        par = childs[child]
        child_files = files[child] if child in files else defaultdict(int)
        par_files = files[par] if par in files else defaultdict(int)
        files[par] = add_maps(par_files, child_files)
        degrees[par] -= 1
        if degrees[par] == 0:
            queue.append(par)

    for dir in queries:
        folder = dir.split("/")[-1]
        if folder in files:
            folder_files = files[folder]
            print(len(folder_files), sum(folder_files.values()))
        else:
            print(0, 0)


if __name__ == '__main__':
    pars = defaultdict(list)
    n, m = list(map(int, input().strip().split()))
    arr = [input().strip().split() for _ in range(m + n)]
    k = int(input())
    queries = [input().strip() for _ in range(k)]
    solution(n, m, arr, queries)
