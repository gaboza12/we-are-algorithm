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
    def check(x, y, z):
        return x + y > z and x + z > y and y + z > x

    arr.sort()
    ans = 0
    if n < 3:
        ans = n
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            count = 2
            for k in range(j + 1, n):
                if check(arr[i], arr[j], arr[k]):
                    count += 1
                else:break
            print(i, j, count)
            ans = max(ans, count)

    return ans
if __name__ == '__main__':
    # n, m = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(n, arr))
