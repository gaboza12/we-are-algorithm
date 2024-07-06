# https://www.acmicpc.net/problem/1918

'''
1. 아이디어 :
    우선순위 맵과, 스택 사용
2. 시간복잡도 :
    O ( n )
3. 자료구조 :
    해시맵, 스택
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(s):

    ans = ""
    stack = []
    operations = {"(" : 0, ")" : 0, "+" : 1, "-" : 1, "*" : 2, "/" : 2}

    for c in s:
        if c.isalnum():
            ans += c

        elif c == "(":
            stack.append(c)

        elif c == ")":
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
        else:
            while stack and operations[stack[-1]] >= operations[c]:
                ans += stack.pop()
            stack.append(c)

    while stack:
        ans += stack.pop()

    return ans


s = input().strip()
print(solution(s))
