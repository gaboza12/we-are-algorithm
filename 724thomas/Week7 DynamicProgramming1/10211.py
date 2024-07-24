# https://www.acmicpc.net/problem/10211

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
    cmax = arr[0]
    base = arr[0]

    for i in range(1, n):
        base = max(base + arr[i], arr[i])
        cmax = max(cmax, base)

    return cmax

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))


