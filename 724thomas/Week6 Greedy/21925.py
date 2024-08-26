# https://www.acmicpc.net/problem/21925

'''
1. 아이디어 :
    스택 사용
2. 시간복잡도 :
    O( n * n )
3. 자료구조 :
    스택
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    def check():
        if len(stack) % 2 == 1:
            return False
        for i in range(len(stack) // 2):
            if stack[i] != stack[-1 - i]:
                return False
        return True

    stack = []
    count = 0
    for n in arr:
        stack.append(n)
        if check():
            count += 1
            stack.clear()

    return count if not stack else -1


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))
