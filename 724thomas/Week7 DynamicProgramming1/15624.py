# https://www.acmicpc.net/problem/15624

'''
1. 아이디어 :
    피보나치 수열을 행렬 형태로 표현합니다.
    행렬 거듭제곱을 사용하여 n번째 피보나치 수를 빠르게 계산합니다.
2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
input = sys.stdin.readline

MOD = 1000000007

def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

def matrix_pow(M, power):
    result = [[1, 0], [0, 1]]
    base = M

    while power:
        if power % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        power //= 2

    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    F = [[1, 1], [1, 0]]
    result = matrix_pow(F, n-1)
    return result[0][0]

n = int(input())
print(fibonacci(n))