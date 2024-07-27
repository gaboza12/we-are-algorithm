# https://www.acmicpc.net/problem/15489

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
input = sys.stdin.readline

def solution(r, c, v):
    # 파스칼의 삼각형 생성
    pascal = [[0] * (r + v) for _ in range(r + v)]
    pascal[0][0] = 1

    for i in range(1, r + v):
        pascal[i][0] = 1
        for j in range(1, i + 1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    total_sum = 0
    for i in range(r - 1, r - 1 + v):
        for j in range(c - 1, c - 1 + (i - (r - 1)) + 1):
            total_sum += pascal[i][j]
    return total_sum

# 입력 받기
r, c, v = map(int, input().split())
print(solution(r, c, v))


