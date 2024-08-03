# https://www.acmicpc.net/problem/2624

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

def solution(target, coins):
    dp = [[0 for _ in range(len(coins))] for _ in range(target+1)]
    print(*dp, sep="\n")
    return 1

if __name__ == '__main__':
    target = int(input())
    coins = []
    for _ in range(int(input())):
        coins.append(list(map(int, input().strip().split())))
    print(solution(target, coins))


