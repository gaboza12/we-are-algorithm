# https://www.acmicpc.net/problem/5635

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


def solution(arr):
    def convert(day, month, year):
        return int(year) * 365 + int(month) * 31 + int(day)

    ans = []
    for name, day, month, year in arr:
        ans.append((convert(day, month, year), name))

    ans.sort(reverse=True)
    print(ans[0][-1])
    print(ans[-1][-1])

if __name__ == '__main__':
    n = int(input())
    arr = [input().strip().split() for _ in range(n)]
    solution(arr)

