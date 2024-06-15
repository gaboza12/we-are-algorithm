# https://www.acmicpc.net/problem/22942

'''
1. 아이디어 :
    괄호라고 생각하고 스택을 사용
2. 시간복잡도 :
    O ( nlogn )
3. 자료구조 :
    스택
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(pairs):

    circles = []
    for i, pair in enumerate(pairs):
        x, r = pair
        circles.append((x-r, i))
        circles.append((x+r, i))
    circles.sort()

    stack = []

    for c in circles:
        if stack:
            if stack[-1][1] == c[1]:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)

    return "YES" if not stack else "NO"


pairs = []
for _ in range(int(input())):
    pairs.append(list(map(int, input().split())))
print(solution(pairs))





