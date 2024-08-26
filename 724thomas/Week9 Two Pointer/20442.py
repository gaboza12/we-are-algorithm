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


def solution(s):
    left_c = []
    right_c = []
    count = 0
    for c in s:
        if c == "K":
            count += 1
        else:
            left_c.append(count)
    count = 0
    for c in s[::-1]:
        if c == "K":
            count += 1
        else:
            right_c.append(count)
    right_c = right_c[::-1]
    left = 0
    right = len(right_c) - 1
    ans = 0

    while left <= right:
        R_count = right - left + 1
        ans = max(ans, R_count + min(left_c[left], right_c[right]) * 2)
        if left_c[left] < right_c[right]:
            left += 1
        elif left_c[left] > right_c[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return ans


if __name__ == '__main__':
    s = input().strip()
    print(solution(s))
