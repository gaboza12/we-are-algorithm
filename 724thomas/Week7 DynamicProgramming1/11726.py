# https://www.acmicpc.net/problem/11726

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import defaultdict
def solution(n):
    ans = defaultdict(int)
    if n <= 3:
        return n
    a, b = 1, 2
    for i in range(n-2):
        a, b = b, a+b
    return b % 10007

n = int(input())
print(solution(n))


