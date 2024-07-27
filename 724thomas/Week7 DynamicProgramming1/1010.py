# https://www.acmicpc.net/problem/1010

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

import math
def solution(n, m):
    return math.comb(m, n)

for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    print(math.comb(m, n))


