# https://www.acmicpc.net/problem/1966

'''
1. 아이디어 :
    스택 사용
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
    ans = []
    stack = []
    curr = 1

    for n in arr:
        while curr <= n:
            stack.append(curr)
            curr += 1
            ans.append("+")

        if stack and stack[-1] == n:
            stack.pop()
            ans.append("-")
        else:
            return "NO"

    return "\n".join(ans)



arr =[int(input()) for _ in range(int(input()))]
print(solution(arr))





