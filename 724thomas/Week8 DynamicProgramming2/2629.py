# https://www.acmicpc.net/problem/2629

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

from itertools import permutations


def solution(n, weights, targets):
    max_weight = sum(weights)
    dp = [False] * (2 * max_weight + 1)
    dp[max_weight] = True  # 0 무게를 표현하기 위해 중앙에 True 설정

    for weight in weights:
        new_dp = dp[:]
        for i in range(2 * max_weight + 1):
            if dp[i]:
                if i + weight <= 2 * max_weight:
                    new_dp[i + weight] = True
                if i - weight >= 0:
                    new_dp[i - weight] = True
        dp = new_dp

    ans = []
    for t in targets:
        if -max_weight <= t <= max_weight and dp[t + max_weight]:
            ans.append("Y")
        else:
            ans.append("N")
    return ans



if __name__ == '__main__':
    n = int(input())
    weights = list(map(int, input().strip().split()))
    int(input())
    targets = list(map(int, input().strip().split()))
    print(*solution(n, weights, targets))
