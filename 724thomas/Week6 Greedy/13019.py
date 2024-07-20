# https://www.acmicpc.net/problem/13019

'''
1. 아이디어 :
    a= ABCA, b= AABC가 있을떄
    a의 A2개와 B의 A2개가 있으면 나머지는 뒤로 민다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    배열
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import Counter


def solution(a, b):
    if Counter(a) != Counter(b):
        return -1

    a = a[::-1]
    b = b[::-1]

    n = len(a)
    j = 0
    for i in range(n):
        if a[i] == b[j]:
            j += 1

    return n - j


a = [c for c in input().strip()]
b = [c for c in input().strip()]
print(solution(a, b))
