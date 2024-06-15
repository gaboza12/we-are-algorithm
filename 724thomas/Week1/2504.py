# https://www.acmicpc.net/problem/2504

'''
1. 아이디어 :
    스택을 사용해서 [ ] ( ) 트래킹. (return 0)
    curr에 현재 배수를 저장하면서 괄호가 닫힐때마다 누적된 값을 더해줬다.
    s[i-1]을 확인하지 않으면, 이미 중괄호 안에 값이 반영이 되었는데 다시 계산하게 됨.
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

def solution(s):
    stack = []
    ans = 0
    curr = 1

    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
            curr *= 2
        elif s[i] == "[":
            stack.append(s[i])
            curr *= 3
        elif s[i] == ")":
            if not stack or stack[-1] != "(":
                return 0

            if s[i-1] == "(":
                ans += curr
            stack.pop()
            curr //=2
        elif s[i] == "]":
            if not stack or stack[-1] != "[":
                return 0

            if s[i - 1] == '[':
                ans += curr
            stack.pop()
            curr //= 3

    if stack:
        return 0

    return ans

s = input()
print(solution(s))





