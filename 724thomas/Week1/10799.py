# https://www.acmicpc.net/problem/10799

'''
1. 아이디어 :
    - 스택 사용
2. 시간복잡도 :
    O ( n )
3. 자료구조 :
    스택
'''

from collections import deque
import heapq
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(arr):
    arr = arr.replace("()", ".")

    ans = 0
    left = 0

    for c in arr:
        if c == ".":
            ans += left
        if c == "(":
            left += 1
        elif c == ")":
            left -= 1
            ans += 1
    return ans

arr = input()
print(solution(arr))





