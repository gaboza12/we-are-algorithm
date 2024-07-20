# https://www.acmicpc.net/problem/1456

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def solution(n, m):
    max_sqrt = int(m ** 0.5) + 1

    def sieve(max_num):
        is_prime = [True] * (max_num+1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, max_num+1):
            if is_prime[i]:
                for j in range(i*i, max_num+1, i):
                    is_prime[j] = False
        return [num for num, prime in enumerate(is_prime) if prime]

    max_sqrt = int(m ** 0.5) + 1
    primes = sieve(max_sqrt)

    ans = set()
    for prime in primes:
        power = prime * prime
        while power <= m:
            if power >= n:
                ans.add(power)
            if power > m // prime:
                break
            power *= prime

    return len(ans)


n, m = list(map(int, input().split()))
print(solution(n, m))
