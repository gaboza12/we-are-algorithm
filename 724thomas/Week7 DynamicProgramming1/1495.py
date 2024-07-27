# https://www.acmicpc.net/problem/1495

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

def solution(n, s, m, arr):
    prev = set()
    prev.add(s)

    for num in arr:
        curr = set()
        for p in prev:
            if p + num <= m:
                curr.add(p+num)
            if p - num >= 0:
                curr.add(p-num)
        prev = curr
    return max(prev) if prev else -1

if __name__ == '__main__':
    n, s, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solution(n, s, m, arr))


