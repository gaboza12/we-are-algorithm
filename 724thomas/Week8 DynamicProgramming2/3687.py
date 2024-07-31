# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys

input = lambda: sys.stdin.readline().rstrip()

# 각 숫자를 만드는 데 필요한 성냥개비 수
matchsticks = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

# 주어진 성냥개비 개수로 만들 수 있는 가장 작은 숫자
min_map = {2: 1, 3: 7, 4: 4, 5: 2, 6: 6, 7: 8}


def solution(targets):
    # 필요한 최대 성냥개비 수
    dp = [float('inf')] * 101
    init_list = ['', '', 1, 7, 4, 2, 6, 8]
    for i in range(2, 8):
        dp[i] = init_list[i]

    for i in range(8, 101):
        for j in range(2, i - 1):
            dp[i] = min(dp[i], int(str(dp[j]) + str(dp[i - j])))
            if j == 6:
                dp[i] = min(dp[i], int(str(dp[i - j]) + "0"))

    def find_biggest(num):
        ans = '1' * (num//2)
        if num % 2:
            ans = '7' + ans[1:]
        return ans

    ans = []
    for n in targets:
        ans.append((dp[n], find_biggest(n)))
    return ans

if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append(int(input()))
    results = solution(arr)
    for min_val, max_val in results:
        print(min_val, max_val)
