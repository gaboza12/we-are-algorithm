# https://www.acmicpc.net/problem/16194

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
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    for pack in range(1, n+1):
        for i in range(pack, n+1):
            dp[i] = min(dp[i], dp[i-pack] + arr[pack-1])
    return dp[-1]

if __name__ == '__main__':
    n = int(input().rstrip())
    arr = list(map(int, input().split()))
    print(solution(n, arr))


