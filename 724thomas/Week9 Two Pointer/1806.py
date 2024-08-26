# https://www.acmicpc.net/problem/1806

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

def solution(n, m, arr):
    # print(*arr, sep="\n")
    print(arr)
    left = right = 0
    total = 0
    ans = float('inf')
    for right in range(n):
        total += arr[right]
        while total-arr[left] >= m:
            total -= arr[left]
            left += 1
        print(left, right, total)
        if total >= m:
            ans = min(ans, right-left+1)
    return ans if ans != float('inf') else 0

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().strip().split()))
    print(solution(n, m, arr))


