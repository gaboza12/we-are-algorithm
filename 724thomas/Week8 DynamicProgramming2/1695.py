# https://www.acmicpc.net/problem/1695

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
input = lambda: sys.stdin.readline().rstrip()

def min_insertions_to_make_palindrome(arr):
    n = len(arr)
    dp = [0] * n

    for start in range(n - 2, -1, -1):
        prev = 0  # Represents dp[start + 1][end - 1]
        for end in range(start + 1, n):
            temp = dp[end]  # Store the current dp[end] before it gets updated
            if arr[start] == arr[end]:
                dp[end] = prev
            else:
                dp[end] = min(dp[end], dp[end - 1]) + 1
            prev = temp

    return dp[n - 1]

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))
    print(min_insertions_to_make_palindrome(arr))


