# https://www.acmicpc.net/problem/21941

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()


def solution(s, arr):
    n = len(s)
    dp = [i for i in range(n + 1)]

    for i in range(n):
        dp[i+1] = max(dp[i+1], dp[i]+1)

        for target, score in arr:
            length = len(target)
            if i + length <= n and s[i:i+length] == target:
                dp[i+length] = max(dp[i+length], dp[i] + score)

    return dp[-1]

if __name__ == '__main__':
    s = input().strip()
    arr = []
    for _ in range(int(input())):
        a, b = input().split()
        b = int(b)
        if b <= 0:
            continue
        arr.append((a, b))
    print(solution(s, arr))