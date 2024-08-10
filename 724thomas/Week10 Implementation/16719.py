# https://www.acmicpc.net/problem/

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
from collections import defaultdict


def solution(s):
    ans = [""] * len(s)

    def dfs(l, r):
        if l > r:
            return
        min_char = min(s[l:r + 1])
        idx = s.index(min_char, l, r + 1)
        ans[idx] = min_char
        print("".join(ans))
        dfs(idx+1, r)
        dfs(l, idx-1)

    dfs(0, len(s)-1)


if __name__ == '__main__':
    s = input().strip()
    solution(s)
