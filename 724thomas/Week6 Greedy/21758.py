# https://www.acmicpc.net/problem/21758

'''
1. 아이디어 :
    누적합으로 풀 수 있다
    첫번째 벌은 항상 왼쪽 또는 오른쪽 끝이므로,
    1. 벌통이 반대쪽 끝에 있을때 두번째 벌의 누적합을 구하고, 반대 케이스도 구한다
    2. 벌이 양쪽 끝에 있을 경우도 똑같이 구한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    해시맵
'''

import sys

# sys.setrecursionlimit(1000000)
input = sys.stdin.readline

from collections import defaultdict


def solution(n, arr):
    def get_max(arr, total, l):
        ans = 0
        base = total - arr[0]
        for b in range(1, l):
            base -= arr[b]
            prefix_sum[b] = base

        for b in range(1, l):
            ans = max(ans, total - arr[0] - arr[b] + prefix_sum[b])
        return ans

    l = len(arr)
    total = sum(arr)
    prefix_sum = defaultdict(int)

    ans = max(get_max(arr, total, l), get_max(arr[::-1], total, l))

    for b in range(1, l - 1):
        ans = max(ans, total - arr[0] - arr[-1] + arr[b])
    return ans


n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))
