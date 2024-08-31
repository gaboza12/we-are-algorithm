# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

def solution(n, target):
    print(arr)

    def backtrack(arr, shuffles, k):
        if shuffles > k+1:
            return arr
        cards = 2**(k-shuffles+1)
        left = arr[:len(arr)-cards]
        right = arr[len(arr)-cards:]
        return backtrack(right, shuffles+1, k) + left

    init = [i+1 for i in range(n)]
    for i in range(1,10):
        prev = backtrack(init, 1, i)
        for j in range(1,10):
            if backtrack(prev, 1, j) == target:
                return [i,j]


if __name__ == '__main__':
    # n, m = map(int, input().split())
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solution(n, arr))

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
