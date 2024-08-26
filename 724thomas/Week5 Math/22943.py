# https://www.acmicpc.net/problem/22943

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from itertools import permutations


def solution(k, m):
    def sieve(n):  # 에라토스테네스의 체를 사용하여 2부터 n까지의 소수를 구함]
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        return is_prime

    def prime_sums(n):  # 주어진 숫자 n이 두 소수의 합으로 나타낼 수 있는지 확인
        return (n != 4 and primes[n - 2]) or (n >= 7 and n % 2 == 0)
        # n이 소수면, n+2의 합으로 나타낼 수 있다. 4는 예외
        # 골드바흐의 추측에 따르면 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다. (아직 증명X)
        # 4, 6은 같은 소수가 두번 등장해서 X. 7부터 가능하다
    '''
    def prime_sums(n):
        if n <= 2:
            return False
        return primes[n-2] or (n % 2 == 0)
    '''
    def valid_nums(n):  # n을 M으로 나누어 떨어지지 않을 때까지 나눈 후, 그 결과가 두 소수의 곱인지 확인
        temp = n
        while temp % m == 0:
            temp = temp // m

        for i in range(2, int(temp ** 0.5) + 1):
            if temp % i == 0:
                if primes[i] and primes[temp // i]:
                    return True
                return False

    primes = sieve(10 ** k)
    valid_numbers = 0

    for num in permutations('0123456789', k):
        if num[0] == '0':
            continue
        number = int(''.join(num))
        if prime_sums(number) and valid_nums(number):
            valid_numbers += 1

    return valid_numbers


k, m = list(map(int, input().split()))
print(solution(k, m))
