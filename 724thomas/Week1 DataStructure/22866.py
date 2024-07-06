# https://www.acmicpc.net/problem/22866

'''
1. 아이디어 :
    카운터와, 왼쪽배열, 오른쪽배열, 스택을 사용해서, 한 방향으로 순회하면서 가까운 탑의 인덱스를 저장한다.
2. 시간복잡도 :
    O( n )
3. 자료구조 :
    스택, 해시맵
'''


import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
from collections import defaultdict

def solution(arr):
    counter = defaultdict(int)
    stack = []
    left = [None] * len(arr)
    for i, h in enumerate(arr):
        while stack and stack[-1][0] <= h:
            stack.pop()

        if stack:
            left[i] = stack[-1]
        counter[i+1] += len(stack)
        stack.append((h,i+1))

    stack = []
    right = [None] * len(arr)
    for i, h in enumerate(reversed(arr)):
        while stack and stack[-1][0] <= h:
            stack.pop()

        if stack:
            right[i] = stack[-1]
        counter[len(arr) - i] += len(stack)
        stack.append((h,len(arr)- i))
    right = right[::-1]


    for i in range(len(left)):
        if left[i] is None and right[i] is None:
            print(0)
        elif left[i] is not None and right[i] is None:
            print(counter[i+1], left[i][1])
        elif left[i] is None and right[i] is not None:
            print(counter[i+1], right[i][1])
        elif left[i] is not None and right[i] is not None:
            if abs(i + 1 - left[i][1]) <= abs(i + 1 - right[i][1]):
                print(counter[i+1], left[i][1])
            else:
                print(counter[i+1], right[i][1])


input()
arr = list(map(int, input().strip().split()))
solution(arr)


