# https://www.acmicpc.net/problem/17626

'''
1. 아이디어 :
    dp로 풀면 시간초과
    n ** 0.5 ** 2 == n 이면 1개면 충분
    n을 제곱수들로 뺀 후에, n ** 0.5 ** 2 == n 이면 2개
    n을 제곱수 2개로 뺸 후에 n ** 0.5 ** 2 == n 이면 3개
    그 외는 4개로 풀어야 한다
2. 시간복잡도 :
    O( n**3 )
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


import math

def solution(n):
    # 주어진 수가 완전 제곱수인 경우 1 반환
    if int(math.sqrt(n)) ** 2 == n:
        return 1

    # 두 개의 제곱수 합으로 표현되는지 확인
    for i in range(1, int(math.sqrt(n)) + 1):
        if int(math.sqrt(n - i * i)) ** 2 == (n - i * i):
            return 2

    # 세 개의 제곱수 합으로 표현되는지 확인
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i * i)) + 1):
            if int(math.sqrt(n - i * i - j * j)) ** 2 == (n - i * i - j * j):
                return 3

    # 위 조건에 해당되지 않으면 네 개의 제곱수 합
    return 4

n = int(input())
print(solution(n))
