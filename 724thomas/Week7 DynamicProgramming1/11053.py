# https://www.acmicpc.net/problem/11053

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
    stack = [arr[0]]

    for num in arr:
        for i in range(len(stack)):
            if num <= stack[i]:
                stack[i] = num
                break
        else:
            stack.append(num)
    return len(stack)

n = int(input())
arr = list(map(int, input().strip().split()))
print(solution(n, arr))


