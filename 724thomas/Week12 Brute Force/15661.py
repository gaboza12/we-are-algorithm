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
    print(*arr, sep="\n")

    def calc(comb):
        s = l = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if comb[i] == comb[j] == 1:
                    s += arr[i][j] + arr[j][i]
                elif comb[i] == comb[j] == 0:
                    l += arr[i][j] + arr[j][i]
        return abs(s - l)


    def backtrack(s, l, count):
        if count == n:
            if s == 0:
                return
            if l == 0:
                return
            ans[0] = min(ans[0], calc(temp))
            return

        temp.append(1)
        backtrack(s + 1, l, count + 1)
        temp[-1] = 0
        backtrack(s, l+1, count + 1)
        temp.pop()

    ans = [float('inf')]
    temp = [1]
    backtrack(1, 0, 1)
    temp = [0]
    backtrack(0, 1, 1)
    return ans[0]


if __name__ == '__main__':
    # n, m = map(int, input().split())
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(solution(n, arr))

# n = int(input().rstrip())
#
# n, m = map(int, input().split())
# n, m = list(map(int, input().split()))
# a = [c for c in input().strip()]
#
# s = input().rstrip()

# arr = list(map(int, input().strip().split()))
# arr = tuple(map(int, input().split()))
# integer_list = [int(num) for num in input().split()]
# dp = [[0 for _ in range(n)] for _ in range(n)]
# dp = [[0 for j in range(n)] for i in range(n)]
# grid = [list(input().rstrip()) for _ in range(n)] # "aaa" "bbb"
# grid = list(list(map(int, input().split())) for _ in range(n)) # "0 0 0 0", "0 0 0 0"
