# https://www.acmicpc.net/problem/2812

'''
1. 아이디어 :
    스택 사용
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    스택
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, num):
    stack = []
    temp = m
    for i in range(n):
        while stack and m and stack[-1] < num[i]:
            stack.pop()
            m -= 1
        stack.append(num[i])
    return "".join(stack[:n - temp])


n, m = list(map(int, input().split()))
num = str(input().strip())
print(solution(n, m, num))
