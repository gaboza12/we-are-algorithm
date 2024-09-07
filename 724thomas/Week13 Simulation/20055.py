# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from collections import deque


def solution(N, K, durability):
    belt = deque(durability)
    robots = deque([False] * N)  # 로봇이 있는 위치를 저장하는 리스트
    step = 0

    while True:
        step += 1

        belt.rotate(1)
        robots.rotate(1)
        robots[-1] = False

        for i in range(N - 2, -1, -1):
            if robots[i] and not robots[i + 1] and belt[i + 1]:
                robots[i] = False
                robots[i + 1] = True
                belt[i + 1] -= 1
                if belt[i+1] == 0:
                    K -= 1

        robots[-1] = False

        if belt[0] > 0:
            robots[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                K -= 1

        if K <= 0:
            return step

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    print(solution(n, m, arr))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
