# https://www.acmicpc.net/problem/1699

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

def solution(n):
    def get_squares(n):
        ans = []
        for i in range(1, int((n**0.5)) + 1):
            ans.append(i*i)
        return ans

    sqaures = get_squares(n)

    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for square in sqaures:
        for i in range(square, n+1):
            dp[i] = min(dp[i], dp[i-square] + 1)

    return dp[-1]


if __name__ == '__main__':
    print(solution(int(input())))