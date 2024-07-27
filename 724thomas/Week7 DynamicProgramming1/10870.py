# https://www.acmicpc.net/problem/10870

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b

n = int(input())
print(solution(n))


