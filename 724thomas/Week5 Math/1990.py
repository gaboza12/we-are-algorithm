# https://www.acmicpc.net/problem/1990

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(a, b):
    b = min(b, 10000000)

    def sieve(min_num, max_num):
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False
        ans = []
        for i in range(min_num, len(is_prime)):
            if is_prime[i]:
                ans.append(i)
        return ans

    primes = sieve(a, b)
    for p in primes:
        if str(p) == str(p)[::-1]:
            print(p)
    return -1


a, b = list(map(int, input().split()))
print(solution(a, b))
