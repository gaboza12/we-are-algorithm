# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
input = lambda: sys.stdin.readline().rstrip()
def solution(arr):
    cmax = max(5, max(arr)+1)
    dp = [0] * cmax
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7

    for i in range(5, cmax):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

    for n in arr:
        print(dp[n] % 1000000009 )

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append(int(input()))
    solution(arr)


