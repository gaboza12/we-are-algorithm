# https://www.acmicpc.net/problem/11722

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

from bisect import bisect_left
def solution(n, arr):
    arr = arr[::-1]
    stack = []
    for num in arr:
        pos = bisect_left(stack, num)
        if pos == len(stack):
            stack.append(num)
        else:
            stack[pos] = num

    return len(stack)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))


