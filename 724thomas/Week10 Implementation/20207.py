# https://www.acmicpc.net/problem/

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
    dp = [0] * (max([temp[1] for temp in arr])+2)
    for start, end in arr:
        dp[start] += 1
        dp[end+1] -= 1
    for i in range(1, len(dp)):
        dp[i] += dp[i-1]

    ans = 0
    max_height = 0
    length = 0
    for n in dp:
        if n == 0:
            ans += length * max_height
            length = 0
            max_height = 0
        else:
            length += 1
            max_height=max(max_height, n)

    ans += length * max_height
    return ans

if __name__ == '__main__':
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))

