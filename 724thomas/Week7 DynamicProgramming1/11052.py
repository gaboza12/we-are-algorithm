# https://www.acmicpc.net/problem/11052
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
    dp = [0] * (n+1)
    for card in range(1, n+1):
        for i in range(card, n+1):
            dp[i] = max(dp[i], dp[i-card] + arr[card-1])

    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))


