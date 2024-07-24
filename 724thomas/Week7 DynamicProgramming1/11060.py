# https://www.acmicpc.net/problem/11060

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, arr):
    dp = [float('inf')] * (n)
    dp[0] = 0
    for i in range(n):
        jump = arr[i]
        for j in range(i+1, min(n, i+jump+1)):
            dp[j] = min(dp[j], dp[i] + 1)
        print(dp, i)


    return dp[n-1] if dp[n-1] != float('inf') else -1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))


