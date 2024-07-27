# https://www.acmicpc.net/problem/2876

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
from collections import defaultdict

def solution(arr):
    prev = defaultdict(int)
    students = -1
    grade = -1
    for i in range(len(arr)):
        grade_a, grade_b = arr[i]
        curr = defaultdict(int)
        curr[grade_a] = prev[grade_a] + 1
        curr[grade_b] = prev[grade_b] + 1

        if curr[grade_a] > students or (curr[grade_a] == students and grade_a < grade):
            students = curr[grade_a]
            grade = grade_a
        if curr[grade_b] > students or (curr[grade_b] == students and grade_b < grade):
            students = curr[grade_b]
            grade = grade_b

        prev = curr
    return students, grade


if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(int, input().strip().split())))
    print(*solution(arr))
