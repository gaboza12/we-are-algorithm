# https://www.acmicpc.net/problem/1932

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

def solution(n, arr):
    for row in range(n-2,-1,-1):
        for col in range(row+1):
            arr[row][col] += max(arr[row+1][col], arr[row+1][col+1])
    return arr[0][0]

if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(list(map(int, input().strip().split())))
    print(solution(n, arr))


