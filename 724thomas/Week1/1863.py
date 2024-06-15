# https://www.acmicpc.net/problem/1863

'''
1. 아이디어 :
    스택사용
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    스택
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(coordinates):
    ans = 0
    stack = []

    for x,y in coordinates:
        while stack and stack[-1] > y:
            stack.pop()
        if not stack or stack[-1] < y:
            stack.append(y)
            if y != 0:
                ans += 1
    return ans


coordinates = []
for _ in range(int(input())):
    coordinates.append(list(map(int, input().split())))

print(solution(coordinates))


