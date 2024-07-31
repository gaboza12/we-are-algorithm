# https://www.acmicpc.net/problem/20542

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(n, m, s1, s2):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (s1[i - 1] == s2[j - 1]) or (s1[i - 1] == 'i' and s2[j - 1] in 'ijl') or (s1[i - 1] == 'v' and s2[j - 1] == 'w'):
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,   # 삭제
                               dp[i][j - 1] + 1,   # 삽입
                               dp[i - 1][j - 1] + 1)  # 변환

    return dp[n][m]

if __name__ == '__main__':
    n, m = map(int, input().split())
    s1 = input().strip()
    s2 = input().strip()
    print(solution(n, m, s1, s2))


