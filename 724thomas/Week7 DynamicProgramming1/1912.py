# https://www.acmicpc.net/problem/1912

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''


import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr):
    total = 0
    ans = -float('inf')
    for num in arr:
        total += num
        ans = max(ans, total)
        total = max(total, 0)
    return ans

n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))


