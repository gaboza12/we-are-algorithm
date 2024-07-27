# https://www.acmicpc.net/problem/2407

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, m):

    def factorial(num):
        if num <= 1:
            return 1
        ans = 1
        for i in range(2, num + 1):
            ans *= i
        return ans

    return factorial(n) // (factorial(m) * factorial(n-m))

n, m = list(map(int, input().split()))
print(solution(n, m))


