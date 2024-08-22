# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

def solution(n, m, arr):
    queue = deque()
    visited = set()
    for n in arr:
        queue.append((n, 0))
        visited.add(n)

    dir = [-1, 1]

    ans = 0
    while queue:
        curr, cost = queue.popleft()
        for x in dir:
            if curr+x in visited or not m:
                continue
            visited.add(curr+x)
            queue.append((curr+x, cost + 1))
            ans += cost+1
            m -= 1
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = tuple(map(int, input().split()))
    print(solution(n, m, arr))

