# https://www.acmicpc.net/problem/2491

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
    inc = 1
    dec = 1
    cmax = 1
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            inc += 1
            dec = 1
        elif arr[i] > arr[i+1]:
            inc = 1
            dec += 1
        else:
            inc += 1
            dec += 1
        cmax = max(cmax, inc, dec)

    return cmax

n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))


