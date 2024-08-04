# https://www.acmicpc.net/problem/22862

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


def solution(n, k, arr):
    odd_count = 0
    left = right = 0
    ans = 0
    while right < n:
        if arr[right] % 2 == 0:
            right += 1
        else:
            if odd_count<k:
                odd_count+=1
                right += 1
            else:
                if arr[left] % 2 != 0:
                    odd_count-=1
                left += 1
        ans = max(ans, right - left - odd_count)
    return ans


if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    print(solution(n, m, arr))
