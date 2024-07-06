# https://www.acmicpc.net/problem/14595

'''
1. 아이디어 :
    interval로 풀 수 있다
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, ranges):
    if not ranges:
        return n

    ranges.sort()
    ps, pe = ranges[0]
    for ns, ne in ranges[1:]:
        if pe < ns:
            n -= (pe-ps)
            ps = ns
            pe = ne
        else:
            pe = max(pe, ne)
    n -= (pe-ps)
    return n


n = int(input())
m = int(input())
ranges = []
for i in range(m):
    ranges.append(list(map(int, input().strip().split())))
print(solution(n, m, ranges))
