# https://www.acmicpc.net/problem/14719

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
    left = [0]
    right = [0]
    for i in range(m-1):
        left.append(max(left[-1], arr[i]))
        right.append(max(right[-1], arr[-1-i]))
    return sum([max(0, min(left[i], right[-1-i]) - arr[i]  ) for i in range(m)])

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = tuple(map(int, input().split()))
    print(solution(n, m, arr))

