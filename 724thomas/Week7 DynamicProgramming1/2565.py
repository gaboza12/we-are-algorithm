# https://www.acmicpc.net/problem/2565

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

from bisect import bisect_left
def solution(n, arr):
    arr.sort()
    b_values = [x[1] for x in arr]

    stack = []
    for v in b_values:
        pos = bisect_left(stack, v)
        if pos == len(stack):
            stack.append(v)
        else:
            stack[pos] = v

    return n - len(stack)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))
