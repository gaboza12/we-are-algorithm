# https://www.acmicpc.net/problem/

'''
1. 아이디어 :

2. 시간복잡도 :
    O(
3. 자료구조 :

'''

import sys
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def solution(n, arr, p, m):

    ans = []
    stack = [arr[0]]
    visited = set()
    visited.add(0)
    def backtrack(idx, plus, multiply, total):
        if idx == len(arr):
            ans.append(stack.copy())
            return

        for i, num in enumerate(arr):
            if i in visited:
                continue
            if plus:
                visited.add(i)
                stack[-1] += num
                backtrack(idx+1, plus-1, multiply, total + num)
                stack[-1] -= num
                visited.remove(i)
            if multiply:
                visited.add(i)
                stack.append(num)
                backtrack(idx+1, plus, multiply-1, total * num)
                stack.pop()
                visited.remove(i)

    def multiply_list(arr):
        ans = 1
        for n in arr:
            ans *= n
        return ans

    backtrack(1, p, m, arr[0])
    cmax = 0
    for a in ans:
        cmax = max(cmax, multiply_list(a))

    return cmax

n = int(input())
arr = list(map(int, input().strip().split()))
p, m = list(map(int, input().strip().split()))
print(solution(n, arr, p, m))
