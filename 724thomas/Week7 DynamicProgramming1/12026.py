# https://www.acmicpc.net/problem/12026

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

def solution(n, s):
    def get_next(s):
        if s == "B":
            return "O"
        if s == "O":
            return "J"
        if s == "J":
            return "B"

    dp = [float('inf')] * (n+1)
    dp[-1] = 0
    for i in range(n-1,0,-1):
        next = get_next(s[i-1])
        for j in range(i+1, n+1):
            if s[j-1] == next:
                dp[i] = min(dp[i], dp[j] + (j-i)**2)
    return dp[1] if dp[1] != float('inf') else -1

if __name__ == '__main__':
    n = int(input())
    s = input().strip()
    print(solution(n, s))


