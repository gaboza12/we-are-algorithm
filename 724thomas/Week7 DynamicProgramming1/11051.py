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


def solution(n, m):
    # n! / (n-k)! * k!

    def factorial(n):
        ans = 1
        for i in range(2, n + 1):
            ans *= i
        return ans

    return (factorial(n) // factorial(n - m)// factorial(m)) % 10007


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    print(solution(n, m))
