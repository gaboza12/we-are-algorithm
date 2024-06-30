# https://www.acmicpc.net/problem/3108

'''
1. 아이디어 :
    사격형의 갯수 = 펜을 들어야하는 횟수
    두개의 사각형이 겹치거나 맞닿으면 펜을 들어야하는 횟수 - 1
    각 사각형이 0,0,0,0 (점)과 닿는지 확인하여 닿으면 -1
2. 시간복잡도 :
    O( n**2 )
3. 자료구조 :
    배열
'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, squares):
    def is_collide(square1, square2):
        x1_1, y1_1, x2_1, y2_1 = square1
        x1_2, y1_2, x2_2, y2_2 = square2
        if x2_1 < x1_2 or x1_1 > x2_2 or y2_1 < y1_2 or y1_1 > y2_2:
            return False
        if x1_1 < x1_2 and y1_1 < y1_2 and x2_1 > x2_2 and y2_1 > y2_2:
            return False
        if x1_2 < x1_1 and y1_2 < y1_1 and x2_2 > x2_1 and y2_2 > y2_1:
            return False
        return True

    def find(x):
        if x != par[x]:
            par[x] = find(par[x])
        return par[x]

    def union(a, b):
        ra = find(a)
        rb = find(b)
        if ra == rb:
            return False
        if rank[ra] > rank[rb]:
            par[rb] = ra
        elif rank[ra] < rank[rb]:
            par[ra] = rb
        else:
            par[rb] = ra
            rank[ra] += 1
        return True

    par = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    ans = n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if is_collide(squares[i], squares[j]):
                if union(i, j):
                    ans -= 1

    for square in squares:
        if is_collide(square, [0,0,0,0]):
            ans-=1
            break

    return ans


n = int(input())
squares = []
for _ in range(n):
    squares.append(list(map(int, input().strip().split())))
print(solution(n, squares))
