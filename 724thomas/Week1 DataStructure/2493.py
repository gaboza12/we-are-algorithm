# https://www.acmicpc.net/problem/2493

'''
1. 아이디어 :
    monotonic stack 사용
2. 시간복잡도 :
    O ( n )
3. 자료구조 :
    스택
'''

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(heights):
    ans = []
    stack = []

    for i, h in enumerate(heights):
        while stack and stack[-1][0] < h:
            stack.pop()
        if not stack:
            ans.append(0)
        else:
            ans.append(stack[-1][1])
        stack.append((h, i+1))
    return ans

input()
arr = list(map(int, input().strip().split()))
print(*solution(arr))





