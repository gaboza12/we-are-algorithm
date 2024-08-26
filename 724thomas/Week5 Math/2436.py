# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
from math import gcd

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict

def solution(g, l):
    if b % a != 0:
        return -1

    '''
    A = a * g
    B = b * g
    
    l = a * b * g
    '''

a, b = map(int, input().split())
result = solution(a, b)
if result == -1:
    print(result)
else:
    print(result[0], result[1])

a, b = list(map(int, input().split()))
print(solution(a, b))
