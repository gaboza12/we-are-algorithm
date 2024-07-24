# https://www.acmicpc.net/problem/

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


if __name__ == '__main__':
    days = int(input())
    while days != 0:
        cmax = -float('inf')
        total = 0
        for _ in range(days):
            val = int(input())
            total = max(val, total+val)
            cmax = max(cmax, total)
        print(cmax)
        days = int(input())


