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


def solution(n, arr):
    arr.sort()
    ans = float('inf')
    for i in range(n):
        for j in range(i + 3, n):
            left = i + 1
            right = j - 1
            while left < right:
                elsa = arr[i] + arr[j]
                anna = arr[left] + arr[right]
                if ans > abs(elsa-anna):
                    ans = abs(elsa-anna)
                # ans = min(ans, abs(elsa - anna))

                if elsa < anna:
                    right -= 1
                else:
                    left += 1

    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(solution(n, arr))
