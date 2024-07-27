# https://www.acmicpc.net/problem/1309

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


def solution(n):
    prev = [1, 0, 0]
    for i in range(1, n+1):
        curr = [sum(prev), prev[0] + prev[2], prev[0] + prev[1]]
        prev = curr
    return sum(prev)


if __name__ == '__main__':
    print(solution(int(input())))
