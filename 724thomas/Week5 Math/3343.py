# https://www.acmicpc.net/problem/3343

'''
1. 아이디어 :
    가성비가 좋은 쪽을 a로 둔다
    c를 c-1개까지 구매하는 경우를 탐색한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    -
'''

import sys

input = sys.stdin.readline

import math
def solution(n, a, b, c, d):

    if b * c < d * a:
        a, b, c, d = c, d, a, b

    min_cost = float('inf')

    for i in range(c):
        remaining = n - i * a
        if remaining < 0:
            break
        cost = i * b
        if remaining > 0:
            cost += math.ceil(remaining / c) * d
        min_cost = min(min_cost, cost)

    return min_cost


n, a, b, c, d = list(map(int, input().strip().split()))
print(solution(n, a, b, c, d))
