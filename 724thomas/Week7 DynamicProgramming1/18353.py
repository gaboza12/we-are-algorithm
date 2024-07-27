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

import bisect


def solution(n, arr):

    def lis():
        ans = []
        for num in arr:
            pos = bisect.bisect_left(ans, num)
            if pos == len(ans):
                ans.append(num)
            else:
                ans[pos] = num
        return ans

    arr = arr[::-1]
    return len(arr) - len(lis())


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))
