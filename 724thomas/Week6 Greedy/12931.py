# https://www.acmicpc.net/problem/12931

'''
1. 아이디어 :
    각 숫자에 대해, 2로 나누는 횟수와 1을 뺴는 횟수를 구한다.
    모든 숫자의 1을 빼는 횟수 + 모든 숫자의 2로 나누는 횟수의 최댓값
2. 시간복잡도 :
    O( n * n )
3. 자료구조 :
    -
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, arr):
    def get_one_twp(n):
        ans = [0, 0]
        while n > 0:
            if n % 2 == 0:
                n = n // 2
                ans[1] += 1
            else:
                n -= 1
                ans[0] += 1
        return ans

    ones = 0
    twos = 0
    for num in arr:
        one, two = get_one_twp(num)
        ones += one
        twos = max(twos, two)

    return ones + twos


n = int(input())
arr = list(map(int, input().strip().split()))

print(solution(n, arr))
