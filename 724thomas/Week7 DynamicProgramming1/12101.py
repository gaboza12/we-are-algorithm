# https://www.acmicpc.net/problem/12101

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(n, m):
    dp = [[] for _ in range(n+1)]
    dp[0] = [[""]]

    for i in range(1, n + 1):
        for j in range(1, 4):
            if i - j >= 0:
                for seq in dp[i - j]:
                    dp[i].append(seq + [str(j)])

    result = []
    for sequences in dp[n]:
        result.append("+".join(sequences[1:]))

    result.sort()

    if m > len(result):
        return -1
    else:
        return result[m - 1]

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    answer = solution(n, m)
    print(answer)

