# https://www.acmicpc.net/problem/1188

'''
1. 아이디어 :
    gcd(n,m) * ( m/gcd(n,m) - 1 )
2. 시간복잡도 :
    O( 1 )
3. 자료구조 :
    -
'''

import sys
input = sys.stdin.readline

def solution(n, m):
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    return m - gcd(n, m)

n, m = list(map(int, input().split()))
print(solution(n, m))
