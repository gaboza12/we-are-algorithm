# https://www.acmicpc.net/problem/

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

MOD = 10007
def solution(n, m, h, blocks):
    '''
    n = 학생수
    m = 블록수
    h = 높이
    '''

    dp = [0] * (h+1)
    dp[0] = 1

    for student in range(n):
        current_blocks = blocks[student]
        for height in range(h, -1, -1):
            for block in current_blocks:
                if height - block >= 0:
                    dp[height] = (dp[height] + dp[height-block]) % MOD

    return dp[h]


if __name__ == '__main__':
    n, m, h = list(map(int, input().strip().split()))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, m, h, arr))
