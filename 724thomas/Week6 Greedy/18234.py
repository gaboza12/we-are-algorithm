# https://www.acmicpc.net/problem/

'''
1. 아이디어 :
    "pi는 항상 wi이상의 값을 가지도록 준비했다." 가 핵심이다.
    무조건 나중에 먹는게 이득이다.
2. 시간복잡도 :
    O( nlogn )
3. 자료구조 :
    -
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m, carrots):
    carrots.sort(key=lambda x: (x[1], x[0]))
    total = 0
    for i in range(n):
        initial, addition = carrots.pop()
        total += initial + addition * (m-i-1)

    return total

n, m = list(map(int, input().split()))
carrots = []
for _ in range(n):
    carrots.append(list(map(int, input().split())))
print(solution(n, m, carrots))
