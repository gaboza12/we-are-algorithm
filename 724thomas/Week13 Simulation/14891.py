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


def solution(arr, commands):
    # print(*arr, sep="\n")
    # print(commands)

    # 1: clock 2: anti-clock

    def check(lcog, rcog):
        return lcog[2] != rcog[6]

    def change(idx, dir):
        # bit = [dir if i % 2 == idx % 2 else -dir for i in range(4)]
        bit = [0, 0, 0, 0]
        queue = deque()
        queue.append((idx, dir))
        visited = set()
        visited.add(idx)

        while queue:
            curr, d = queue.popleft()
            if d == 0:
                bit[curr] = 0
                continue
            bit[curr] = d
            if curr != 0:
                if check(arr[curr - 1], arr[curr]) and curr-1 not in visited:
                    visited.add(curr - 1)
                    queue.append((curr - 1, -d))
            if curr != 3:
                if check(arr[curr], arr[curr + 1]) and curr+1 not in visited:
                    visited.add(curr + 1)
                    queue.append((curr + 1, -d))

        for i, d in enumerate(bit):
            if d == 1:
                arr[i].appendleft(arr[i].pop())
            elif d == -1:
                arr[i].append(arr[i].popleft())

    for idx, dir in commands:
        change(idx-1, dir)
    # print(*arr, sep="\n")

    ans = 0
    for i in range(4):
        ans += int(arr[i][0]) * 2 ** i
    return ans


if __name__ == '__main__':
    # n, m = map(int, input().split())
    arr = [deque(list(input().strip())) for _ in range(4)]
    n = int(input())
    commands = [list(map(int, input().split())) for _ in range(n)]
    print(solution(arr, commands))

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
