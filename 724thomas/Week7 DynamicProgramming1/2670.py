# https://www.acmicpc.net/problem/2670

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr):
    cmax = 0
    base = 0

    for i in range(n):
        base = max(base * arr[i], arr[i])
        cmax = max(cmax, base)

    return '%0.3f' % cmax

n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))
print(solution(n, arr))


